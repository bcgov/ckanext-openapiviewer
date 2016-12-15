# ckanext-openapi

CKAN Extension which creates an OpenAPI (aka Swagger) view that is accessible for previewing
resources of the OpenAPI mimetype.

Installation:

1. Copy ckanext-openapi into the ckan src folder

2. Within src/ckanext-openapi run: 

    python setup.py develop

3. Add 'openapi_view' to the list of plugins in your .ini file

4. Add the new resource view to the CKAN database:

  Paster views create openapi_view -c INI_FILE

5. Startup ckan