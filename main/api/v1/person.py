# coding: utf-8

from __future__ import absolute_import

from google.appengine.ext import ndb
from flask.ext import restful
import flask

from api import helpers
import auth
import model
import util

from main import api_v1


@api_v1.resource('/person/', endpoint='api.person.list')
class PersonListAPI(restful.Resource):
  @auth.login_required
  def get(self):
    person_dbs, person_cursor = model.Person.get_dbs(user_key=auth.current_user_key())
    return helpers.make_response(person_dbs, model.Person.FIELDS, person_cursor)


@api_v1.resource('/person/<string:person_key>/', endpoint='api.person')
class PersonAPI(restful.Resource):
  @auth.login_required
  def get(self, person_key):
    person_db = ndb.Key(urlsafe=person_key).get()
    if not person_db or person_db.user_key != auth.current_user_key():
      helpers.make_not_found_exception('Person %s not found' % person_key)
    return helpers.make_response(person_db, model.Person.FIELDS)


###############################################################################
# Admin
###############################################################################
@api_v1.resource('/admin/person/', endpoint='api.admin.person.list')
class AdminPersonListAPI(restful.Resource):
  @auth.admin_required
  def get(self):
    person_keys = util.param('person_keys', list)
    if person_keys:
      person_db_keys = [ndb.Key(urlsafe=k) for k in person_keys]
      person_dbs = ndb.get_multi(person_db_keys)
      return helpers.make_response(person_dbs, model.person.FIELDS)

    person_dbs, person_cursor = model.Person.get_dbs()
    return helpers.make_response(person_dbs, model.Person.FIELDS, person_cursor)


@api_v1.resource('/admin/person/<string:person_key>/', endpoint='api.admin.person')
class AdminPersonAPI(restful.Resource):
  @auth.admin_required
  def get(self, person_key):
    person_db = ndb.Key(urlsafe=person_key).get()
    if not person_db:
      helpers.make_not_found_exception('Person %s not found' % person_key)
    return helpers.make_response(person_db, model.Person.FIELDS)
