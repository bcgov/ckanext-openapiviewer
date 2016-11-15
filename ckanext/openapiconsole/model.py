import uuid
import datetime

from sqlalchemy import Column
from sqlalchemy import types
from sqlalchemy.ext.declarative import declarative_base

import ckan.model as model
from ckan.lib import dictization
from ckan.plugins import toolkit

log = __import__('logging').getLogger(__name__)

Base = declarative_base()


def make_uuid():
    return unicode(uuid.uuid4())


class OpenApiSpecUrl(Base):
    __tablename__ = 'openapi_spec_url'

    id = Column(types.UnicodeText, primary_key=True, default=make_uuid)
    package_id = Column(types.UnicodeText, nullable=False, index=True)
    openapi_spec_url = Column(types.UnicodeText)

    def __repr__(self):
        return "id:"+self.id+", package:"+self.package_id+", openapi_spec_url:"+self.openapi_spec_url

    def as_dict(self):
        context = {'model': model}
        oapic_dict = dictization.table_dictize(self, context)
        return oapic_dict

    '''Returns the OpenApiSpecUrls for the given package. (may be more than one)'''
    @classmethod
    def get_for_package(cls, package_id):
        matches = model.Session.query(cls) \
            .filter(cls.package_id == package_id) \
            .all()
        return matches

    '''Returns the OpenApiSpecUrl with the given id. (never returns more than one)'''
    @classmethod
    def get_for_id(cls, id):
        return model.Session.query(cls) \
            .filter(cls.id == id) \
            .first()

    #creates a new record if one doesn't already exist, or updates an 
    #existing record if one does already exist
    @classmethod
    def create_or_update(cls, package_id, openapi_spec_url):
      existing_recs = cls.get_for_package(package_id)
      if existing_recs:
        cls.update(package_id, openapi_spec_url)
      else:
        cls.create(package_id, openapi_spec_url)

    @classmethod
    def create(cls, package_id, openapi_spec_url):
      if openapi_spec_url:
        """Adds a new openapi specification url for the given package"""
        item = OpenApiSpecUrl()
        item.package_id = package_id
        item.openapi_spec_url = openapi_spec_url
        model.Session.add(item)

    @classmethod
    def update(cls, package_id, openapi_spec_url):

        """Updates an openapi specification url for the given package"""
        values = {
                   "openapi_spec_url": openapi_spec_url
                 }
        model.Session.query(cls) \
            .filter(cls.package_id == package_id) \
            .update(values)


def init_tables(engine):
    Base.metadata.create_all(engine)
    log.info('Database table is set up')