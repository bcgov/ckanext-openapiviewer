
import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckanext.openapiconsole.model import OpenApiSpecUrl
from ckan.common import request

log = __import__('logging').getLogger(__name__)

class OpenApiConsolePlugin(p.SingletonPlugin, tk.DefaultDatasetForm): 

  #p.implements(p.IDatasetForm)
  p.implements(p.IConfigurer)
  p.implements(p.IPackageController, inherit=True) # to be notified on package create/update/delete/show events
  p.implements(p.ITemplateHelpers)

  def update_config(self, config):

      # Add this plugin's templates dir to CKAN's extra_template_paths, so
      # that CKAN will use this plugin's custom templates.
      # 'templates' is the path to the templates dir, relative to this
      # plugin.py file.
      tk.add_template_directory(config, 'templates')

      # Add this plugin's public dir to CKAN's extra_public_paths, so
      # that CKAN will use this plugin's custom static files.
      tk.add_public_directory(config, 'public')

  def after_create(self, context, pkg_dict):
    if "openapi_spec_url" in request.params:
      OpenApiSpecUrl.create_or_update(pkg_dict['id'], request.params["openapi_spec_url"])

  def after_update(self, context, pkg_dict):
    if "openapi_spec_url" in request.params:
      OpenApiSpecUrl.create_or_update(pkg_dict['id'], request.params["openapi_spec_url"])

  #TODO: capture package 'delete' events, and clean corresponding records from the database table
  # used by this plugin

  def get_helpers(self):     
    return {'get_openapi_specs_for_package': OpenApiSpecUrl.get_for_package}
