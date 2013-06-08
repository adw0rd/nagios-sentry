nagios-sentry
===============

Plugin for Nagios, which check a count of messages in Sentry.

.. image:: https://pypip.in/d/nagios-sentry/badge.png
    :target: http://pypi.python.org/pypi/nagios-sentry


Installation
--------------

Install ``nagios-sentry`` to Sentry venv::

    source /var/www/sentry/bin/activate
    pip install nagios-sentry

Add to ``INSTALLED_APPS`` in config file ``/etc/sentry.conf``::

    INSTALLED_APPS += ('nagios_sentry', )

Copy the file ``check_sentry_messages.py`` to the Nagios plugins directory.

How to use
------------

Go to the Nagios plugins directory and run this example::

    ./check_sentry_messages.py -w 10 -c 20 \
        --sentry /var/www/sentry/bin/sentry --config /etc/sentry.conf --seconds=300

Where:

* ``-w 10`` - Number of messages in Sentry for ``--seconds`` as WARNING;
* ``-c 20`` - Number of messages in Sentry for ``--seconds`` as CRITICAL;
* ``--sentry /var/www/sentry/bin/sentry`` - Path to binary file of Sentry;
* ``--config /etc/sentry.conf`` - Path to config file of Sentry;
* ``--seconds=300`` - Number of seconds offset.

Available additional options:

* ``--project`` - Number of project. Example ``--project=1``;
* ``--level`` - Number of level. 10=DEBUG, 20=INFO, 25=SUCCESS, 30=WARNING, 40=ERROR;
* ``--logger`` - Name of logger. Example ``--logger=SocialAuth``.
