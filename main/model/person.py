# coding: utf-8

from __future__ import absolute_import

from google.appengine.ext import ndb

from api import fields
import model
import util


class Person(model.Base):
  user_key = ndb.KeyProperty(kind=model.User, required=True)
  name = ndb.StringProperty(required=True)
  department = ndb.StringProperty(default='')
  tags = ndb.StringProperty(repeated=True)
  fact = ndb.TextProperty(required=True)
  timestamp = ndb.DateProperty(required=True)

  @classmethod
  def get_dbs(cls, order=None, **kwargs):
    return super(Person, cls).get_dbs(
      order=order or util.param('order') or '-timestamp',
      **kwargs
    )

  FIELDS = {
    'user_key': fields.Key,
    'name': fields.String,
    'department': fields.String,
    'tags': fields.List(fields.String),
    'fact': fields.String,
    'timestamp': fields.DateTime,
  }

  FIELDS.update(model.Base.FIELDS)
