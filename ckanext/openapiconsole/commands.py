import ckan.plugins as p

log = __import__('logging').getLogger(__name__)

class InitDB(p.toolkit.CkanCommand):
    
    """Create the database table needed by the openapi_console plugin
    """
    summary = __doc__.split('\n')[0]
    usage = __doc__
    max_args = 0
    min_args = 0

    def command(self):
        self._load_config()

        import ckan.model as model
        model.Session.remove()
        model.Session.configure(bind=model.meta.engine)
        
        import ckan.model as model
        from ckanext.openapiconsole.model import init_tables
        init_tables(model.meta.engine)
