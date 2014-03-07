import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-themeswitch',
    version='0.1',
    packages=['themeswitch'],
    include_package_data=True,
    license='BSD License',  # example license
    description='a django app that allows for easy switch between themes',
    long_description=README,
    url='https://github.com/nschlemm/django-themeswitch',
    author='Nikolaus Schlemm',
    author_email='capo@coder-nostra.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)