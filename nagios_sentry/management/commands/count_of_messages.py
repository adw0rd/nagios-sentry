import datetime
from optparse import make_option

from django.conf import settings
from django.utils.timezone import utc
from django.core.management.base import BaseCommand

LEVELS = (
    (10, 'DEBUG'),
    (20, 'INFO'),
    (25, 'SUCCESS'),
    (30, 'WARNING'),
    (40, 'ERROR'),
)
LEVELS_HELP = ', '.join(['='.join(map(str, LEVEL)) for LEVEL in LEVELS])

class Command(BaseCommand):
    """Interesting tables:
    * sentry_message
    * sentry_messagecountbyminute
    """
    help = ''

    option_list = BaseCommand.option_list + (
        make_option('--seconds', default=60, type=int, help='Second offset from NOW()'),
        make_option('--project', type=int, help='Limit truncation to only entries from project.'),
        make_option('--level', type=int, help='Number of level. {0}'.format(LEVELS_HELP)),
        make_option('--logger', type=str, help='Name of logger'),
    )

    def handle(self, *args, **options):
        from sentry.models import Event

        project_id = options.get('project')
        level = options.get('level')
        logger = options.get('logger')

        seconds = options.get('seconds')
        if settings.TIME_ZONE == 'UTC':
            now = datetime.datetime.utcnow().replace(tzinfo=utc)
        else:
            now = datetime.datetime.now()
        datetime_offset = now - datetime.timedelta(seconds=seconds)

        queryset = Event.objects.filter(
            datetime__gt=datetime_offset)
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        if logger:
            queryset = queryset.filter(logger=logger)
        if level:
            queryset = queryset.filter(level=level)

        print queryset.count()
