
import ckan.plugins as p
import ckan.plugins.toolkit as tk
import ckan.lib.datapreview as datapreview
from ckan.common import request

log = __import__('logging').getLogger(__name__)

class OpenApiViewPlugin(p.SingletonPlugin): 

  #interfaces
  p.implements(p.IResourceView, inherit=True)
  p.implements(p.IConfigurer, inherit=True)
  p.implements(p.IConfigurable, inherit=True)
  p.implements(p.IPackageController, inherit=True)
 
  #constants
  supported_formats = ['openapi-json']

  # IConfigurer

  def update_config(self, config):   
    #mimetypes.add_type('application/openapi+json', '.json')
    
    p.toolkit.add_public_directory(config, 'public')
    p.toolkit.add_template_directory(config, 'templates')


  # IConfigurable

  def configure(self, config):
    enabled = config.get('ckan.resource_proxy_enabled', False)
    self.proxy_is_enabled = enabled

  # IResourceView (CKAN >=2.3)

  def info(self):
    return {'name': 'openapi_view',
            'title': 'OpenAPI Console',
            'icon': 'file',
            'iframed': True,
            'default_title': p.toolkit._('OpenAPI Console'),
            }

  def can_view(self, data_dict):
    resource = data_dict['resource']
    format_lower = resource.get('format', '').lower()

    if format_lower in self.supported_formats:
      return True
    return False

  def view_template(self, context, data_dict):
    return 'dataviewer/openapi_view.html'

  def add_default_views(self, context, data_dict):
    if "resources" not in data_dict:
      return

    resources = data_dict["resources"]
    for resource in resources:
      if self.can_view({'package': data_dict, 'resource': resource}):
        #add the openapi resource view for this resource
        view = {'title': 'OpenAPI Console',
                'description': '',
                'resource_id': resource['id'],
                'view_type': 'openapi_view'}
        p.toolkit.get_action('resource_view_create')(
            {'defer_commit': True}, view
        )

  def after_update(self, context, data_dict):
    self.add_default_views(context, data_dict)

  def after_create(self, context, data_dict):
    self.add_default_views(context, data_dict)