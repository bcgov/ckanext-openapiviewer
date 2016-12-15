# ckanext-openapi

CKAN Extension which creates an OpenAPI (aka Swagger) view that is accessible for previewing
resources of the OpenAPI mimetype.

Installation:

1. Copy ckanext-openapi into the ckan src folder

2. Add 'openapi_view' to the list of plugins in your .ini file

3. paster views create openapi_view -c /apps/ckan/conf/development.ini

4. startup ckan