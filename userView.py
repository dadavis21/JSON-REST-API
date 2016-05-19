from flask import Blueprint, request, redirect, render_template, url_for, abort
from flask.views import MethodView
from user import User
from cliq import Cliq
from bson.objectid import ObjectId
import json
from json_rest_api import db



user_view = Blueprint('user_view', __name__)

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

    @user_view.route('/users/<id>', methods=['GET'])
    def get(id):
        user = User.objects.get(user_id=id)
        return user.to_json()

    @user_view.route('/users/<id>', methods=['PUT'])
    def put(id):
        user = User.objects.get(user_id=id)
        if 'previous_cliqs' in request.json:
            user.modify(previous_cliqs, request.json['previous_cliqs'])
        if 'first_name' in request.json:
            user.modify(first_name, request.json['first_name'])
        if 'last_name' in request.json:
            user.modify(last_name, request.json['last_name'])
        if 'gender' in request.json:
            user.modify(gender=request.json['gender'])
        if 'phone' in request.json:
            user.modify(phone, request.json['phone'])
        if 'age' in request.json:
            user.modify(age, request.json['age'])
        user.save()
        return user.to_json()

    @user_view.route('/users/<id>', methods=['DELETE'])
    def delete(id):
        user = User.objects.get(user_id=id)
        user.delete()

user_view.add_url_rule('/users/', view_func=UserView.as_view('users'))
