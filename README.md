# ckanext-openapiconsole

CKAN Extension which adds an interactive OpenAPI (AKA Swagger) console
to packages.

Installation:

1. Copy ckanext-openapiconsole into the ckan src folder

2. Add 'openapi_console' to the list of plugins in your .ini file

3. from within the ckanext-openapiconsole folder, run the following:

python setup.py develop

paster initdb -c [your ini file]

4. startup ckan