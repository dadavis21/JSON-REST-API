from flask import Blueprint, request, redirect, render_template, url_for, abort
from flask.views import MethodView
from user import User
from cliq import Cliq
from bson.objectid import ObjectId
import json
from json_rest_api import db

#Converts mongo bson objects to json to return in views
#"dumps" outputs argument to a textfile and converts to json
views = Blueprint('views', __name__)

class UserView(MethodView):
    def post(self):
        if not request.json:
            abort(400)
        user = User(
            user_id= request.json['user_id'],
            previous_cliqs= request.json['previous_cliqs'],
            first_name= request.json['first_name'],
            last_name= request.json['last_name'],
            gender= request.json['gender'],
            phone= request.json['phone'],
            age= request.json['age'],
            _id= ObjectId()
        )
        user.save()
        return user.to_json()

    def get(self):
        user = User.objects.get(user_id=user_id)
        return user.to_json()

    def put(self):
        user = User.objects.get(user_id=user_id)
        if 'previous_cliqs' in request.json:
            user.modify(previous_cliqs, request.json['previous_cliqs'])
        if 'first_name' in request.json:
            user.modify(first_name, request.json['first_name'])
        if 'last_name' in request.json:
            user.modify(last_name, request.json['last_name'])
        if 'gender' in request.json:
            user.modify(gender, request.json['gender'])
        if 'phone' in request.json:
            user.modify(phone, request.json['phone'])
        if 'age' in request.json:
            user.modify(age, request.json['age'])
        user.save()
        return user.to_json()

    def delete(self):
        user = User.objects.get(user_id=user_id)
        user.delete()

views.add_url_rule('/users/', view_func=UserView.as_view('users'))

class CliqView(MethodView):

    def post(self):
        if not request.json:
            abort(400)
        cliq = Cliq (
            cliq_id = request.json['cliq_id'],
            members = request.json['members'],
            bio = request.json['bio'],
            pending_members = request.json['pending_members'],
            last_active = request.json['last_active'],
            _id = ObjectId()
        )
        cliq.save()
        return cliq.to_json()

    def get(self):
        cliq = Cliq.objects.get(cliq_id=cliq_id)
        return cliq.to_json()

    def put(self):
        cliq = Cliq.objects.get(cliq_id=cliq_id)
        if 'members' in request.json:
            user.modify(members, request.json['members'])
        if 'bio' in request.json:
            user.modify(bio, request.json['bio'])
        if 'pending_members' in request.json:
            user.modify(pending_members, request.json['pending_members'])
        if 'last_active' in request.json:
            user.modify(last_active, request.json['last_active'])
        cliq.save()
        return cliq.to_json()

    def delete(self):
        cliq = Cliq.objects.get(cliq_id=cliq_id)
        cliq.delete()

views.add_url_rule('/cliqs', view_func=CliqView.as_view('cliqs'))
