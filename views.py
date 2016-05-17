from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
import user
from bson import json_util
import json

#Converts mongo bson objects to json to return in views
#"dumps" outputs argument to a textfile and converts to json
views = Blueprint('views', __name__)
def to_json(mongoObj):
    return json.dumps(mongoObj, default=json_util.default)

class UserView(MethodView):
    def post(self, user):
        db.users.insert(user)

    def get(self, id):
        user = db.users.findOne({user_id:id})
        return to_json(user)

    def put(self, id, field, update):
        db.users.update(
            {user_id:id},
            {
                '$set': {field:update}
            }
        )

views.add_url_rule('/users/', view_func=UserView.as_view('users'))

class CliqView(MethodView):

    def post(self, cliq):
        db.cliqs.insert(cliq)

    def get(self, id):
        cliq = db.cliqs.findOne({cliq_id:id})
        return to_json(cliq)

    def put(self, id, field, update):
        db.cliqs.update(
            {cliq_id:id},
            {
                '$set': {field:update}
            }
        )

views.add_url_rule('/cliqs', view_func=CliqView.as_view('cliqs'))
