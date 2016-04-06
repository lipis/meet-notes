# coding: utf-8

from datetime import datetime
from flask.ext import wtf
from google.appengine.ext import ndb
import flask
import wtforms

import auth
import config
import model
import util

from main import app


###############################################################################
# Update
###############################################################################
class PersonUpdateForm(wtf.Form):
  name = wtforms.StringField(
    model.Person.name._verbose_name,
    [wtforms.validators.required()],
    filters=[util.strip_filter],
  )
  department = wtforms.StringField(
    model.Person.department._verbose_name,
    [wtforms.validators.optional()],
    filters=[util.strip_filter],
  )
  tags = wtforms.StringField(
    model.Person.tags._verbose_name,
    [wtforms.validators.optional()],
  )
  fact = wtforms.TextAreaField(
    model.Person.fact._verbose_name,
    [wtforms.validators.required()],
    filters=[util.strip_filter],
    description='Supports Markdown',
  )
  timestamp = wtforms.DateField(
    model.Person.timestamp._verbose_name,
    [wtforms.validators.required()],
  )


@app.route('/person/create/', methods=['GET', 'POST'])
@app.route('/person/<int:person_id>/update/', methods=['GET', 'POST'])
@auth.login_required
def person_update(person_id=0):
  if person_id:
    person_db = model.Person.get_by_id(person_id)
  else:
    person_db = model.Person(user_key=auth.current_user_key())

  if not person_db or person_db.user_key != auth.current_user_key():
    flask.abort(404)

  form = PersonUpdateForm(obj=person_db)

  user_dbs, user_cursor = model.User.get_dbs(limit=-1)
  if flask.request.method == 'GET' and not form.errors:
    form.tags.data = config.TAG_SEPARATOR.join(form.tags.data)
    form.timestamp.data = datetime.utcnow()

  if form.validate_on_submit():
    form.tags.data = util.parse_tags(form.tags.data)
    form.populate_obj(person_db)
    person_db.put()
    return flask.redirect(flask.url_for('person_view', person_id=person_db.key.id()))

  return flask.render_template(
    'person/person_update.html',
    title=person_db.name if person_id else 'New Person',
    html_class='person-update',
    form=form,
    person_db=person_db,
  )


###############################################################################
# List
###############################################################################
@app.route('/people/')
@auth.login_required
def person_list():
  person_dbs, person_cursor = model.Person.get_dbs(user_key=auth.current_user_key())
  return flask.render_template(
    'person/person_list.html',
    html_class='person-list',
    title=u'People I’ve met',
    person_dbs=person_dbs,
    next_url=util.generate_next_url(person_cursor),
    api_url=flask.url_for('api.person.list'),
  )


###############################################################################
# View
###############################################################################
@app.route('/person/<int:person_id>/')
@auth.login_required
def person_view(person_id):
  person_db = model.Person.get_by_id(person_id)
  if not person_db or person_db.user_key != auth.current_user_key():
    flask.abort(404)

  return flask.render_template(
    'person/person_view.html',
    html_class='person-view',
    title=person_db.name,
    person_db=person_db,
    api_url=flask.url_for('api.person', person_key=person_db.key.urlsafe() if person_db.key else ''),
  )


###############################################################################
# Admin List
###############################################################################
@app.route('/admin/person/')
@auth.admin_required
def admin_person_list():
  person_dbs, person_cursor = model.Person.get_dbs(
    order=util.param('order') or '-modified',
  )
  return flask.render_template(
    'person/admin_person_list.html',
    html_class='admin-person-list',
    title='Person List',
    person_dbs=person_dbs,
    next_url=util.generate_next_url(person_cursor),
    api_url=flask.url_for('api.admin.person.list'),
  )


###############################################################################
# Admin Update
###############################################################################
class PersonUpdateAdminForm(PersonUpdateForm):
  pass


@app.route('/admin/person/create/', methods=['GET', 'POST'])
@app.route('/admin/person/<int:person_id>/update/', methods=['GET', 'POST'])
@auth.admin_required
def admin_person_update(person_id=0):
  if person_id:
    person_db = model.Person.get_by_id(person_id)
  else:
    person_db = model.Person(user_key=auth.current_user_key())

  if not person_db:
    flask.abort(404)

  form = PersonUpdateAdminForm(obj=person_db)

  user_dbs, user_cursor = model.User.get_dbs(limit=-1)
  if flask.request.method == 'GET' and not form.errors:
    form.tags.data = config.TAG_SEPARATOR.join(form.tags.data)

  if form.validate_on_submit():
    form.tags.data = util.parse_tags(form.tags.data)
    form.populate_obj(person_db)
    person_db.put()
    return flask.redirect(flask.url_for('admin_person_list', order='-modified'))

  return flask.render_template(
    'person/admin_person_update.html',
    title=person_db.name,
    html_class='admin-person-update',
    form=form,
    person_db=person_db,
    back_url_for='admin_person_list',
    api_url=flask.url_for('api.admin.person', person_key=person_db.key.urlsafe() if person_db.key else ''),
  )
