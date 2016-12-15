from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-openapi',
    version=version,
    description="adds an interactive openapi (aka swagger) view to resources of the openapi mimetype",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Brock Anderson',
    author_email='brock@bandersgeo.ca',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.openapi'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        openapi_view=ckanext.openapi.plugin:OpenApiViewPlugin
    ''',
)
