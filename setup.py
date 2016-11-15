from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-openconsole',
    version=version,
    description="adds openapi (fka swagger) visualization",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Brock Anderson',
    author_email='brock@bandersgeo.ca',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.openapiconsole'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        openapi_console=ckanext.openapiconsole.plugin:OpenApiConsolePlugin

        [paste.paster_command]        
        initdb = ckanext.openapiconsole.commands:InitDB
    ''',
)
