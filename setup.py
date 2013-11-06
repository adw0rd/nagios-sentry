from setuptools import setup, find_packages
from nagios_sentry import __version__

long_description = ""
try:
    readme = open("README.rst")
    long_description = str(readme.read())
    readme.close()
except:
    pass

setup(
    name='nagios-sentry',
    version=__version__,
    description="Plugin for Nagios, which check a count of messages in Sentry",
    long_description=long_description,
    keywords='nagios, sentry',
    author='Mikhail Andreev',
    author_email='x11org@gmail.com',
    url='http://github.com/adw0rd/nagios-sentry',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['setuptools', ],
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    scripts=['check_sentry_messages.py'],
)
