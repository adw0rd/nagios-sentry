#!/usr/bin/env python
import sys
import datetime
import subprocess
from optparse import OptionParser

STATUSES = {
    'UNKNOWN': -1,
    'OK': 0,
    'WARNING': 1,
    'CRITICAL': 2,
}

LEVELS = (
    (10, 'DEBUG'),
    (20, 'INFO'),
    (25, 'SUCCESS'),
    (30, 'WARNING'),
    (40, 'ERROR'),
)
LEVELS_HELP = ', '.join(['='.join(map(str, LEVEL)) for LEVEL in LEVELS])

parser = OptionParser()
parser.add_option('-w', dest='warning', help='Number events for WARNING')
parser.add_option('-c', dest='critical', help='Number events for CRITICAL')
parser.add_option('--sentry', dest='sentry_bin', help='Local path to binary file of sentry. Example: "/bin/sentry"')
parser.add_option('--config', dest='config_path', help='Local path to config file of sentry. Example: "/etc/sentry.conf"')
parser.add_option('--seconds', dest='seconds', type=int, default=60, help='Second offset from NOW()')
parser.add_option('--project', dest='project', type=int, help='Limit truncation to only entries from project.')
parser.add_option('--level', dest='level', type=int, help='Number of level. {0}'.format(LEVELS_HELP))
parser.add_option('--logger', dest='logger', help='Name of logger')
options, args = parser.parse_args()

if not options.sentry_bin:
    parser.error('Path tp binary not given')

if not options.config_path:
    parser.error('Path to config not given')

CMD = ['{sentry} --config={config} count_of_messages'.format(
    sentry=options.sentry_bin, config=options.config_path)]
if options.seconds:
    CMD.append('--seconds={o.seconds}'.format(o=options))
if options.project:
    CMD.append('--project={o.project}'.format(o=options))
if options.level:
    CMD.append('--level={o.level}'.format(o=options))
if options.logger:
    CMD.append('--logger={o.logger}'.format(o=options))
result = subprocess.Popen(" ".join(CMD), stdout=subprocess.PIPE, shell=True)
result.wait()

status = 'UNKNOWN'
output = result.stdout.read().strip(' \t\n\r')

if str(output).isdigit():
    output = int(output)
    if output >= int(options.critical):
        status = 'CRITICAL'
    elif output >= int(options.warning):
        status = 'WARNING'
    else:
        status = 'OK'
print '{0}: {1}'.format(status, output)
sys.exit(STATUSES.get(status, -1))
