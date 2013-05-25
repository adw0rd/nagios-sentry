Installation
-------------

Copy directory ``nagios_sentry`` to site-packages of Sentry venv.
Copy file ``plugin/sentry.py`` to nagios plugins dir.

How to use
-----------

Example::

    ./sentry.py -w 10 -c 20 --sentry /var/www/sentry/bin/sentry --config /etc/sentry.conf --seconds=300

Where:

* ``-w 10`` - Number of messages in Sentry for ``--seconds`` as WARNING;
* ``-c 10`` - Number of messages in Sentry for ``--seconds`` as CRITICAL;
