
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
  p.implements(p.IResourceController, inherit=True)
 
  #constants
  supported_formats = ['openapi-json']
  view_type = 'openapi_view';

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
    return {'name': self.view_type,
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

  # IResourceController

  def after_update(self, context, resource):
    self.add_default_views(context, resource)

  def after_create(self, context, resource):
    self.add_default_views(context, resource)

  # Other functions

  #returns true if the resource already has a view of type 'openapi_view', 
  #and false otherwise
  def has_view_already(self, context, resource):
      if 'id' in resource:
        params = {'id': resource['id']}
        resourceViews = p.toolkit.get_action('resource_view_list')(
            context, params
        )
        for resourceView in resourceViews:
          if "view_type" in resourceView and resourceView["view_type"] == self.view_type:
            return True

      return False

  def add_default_views(self, context, resource):
   
    if 'id' in resource and self.can_view({'resource': resource}) and not self.has_view_already(context, resource):

      #add the openapi resource view for this resource
      view = {'title': 'OpenAPI Console',
              'description': '',
              'resource_id': resource['id'],
              'view_type': self.view_type}
      p.toolkit.get_action('resource_view_create')(
          context, view
      )

