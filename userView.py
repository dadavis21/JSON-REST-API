from flask import Blueprint, request, abort, jsonify
from flask.views import MethodView
from user import User
from cliq import Cliq
from bson.objectid import ObjectId
from json_rest_api.auth import auth
import json

user_view = Blueprint('user_view', __name__)

class UserView(MethodView):
    @auth.login_required
    def post(self):
        if not request.json:
            abort(400)
        user = User.objects(user_id=request.json['user_id'])
        if user.first() != None:
            return jsonify({'Result':'User ID already exists'})
        user = User(
            user_id= request.json['user_id'],
            cliqs= request.json['cliqs'],
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
    @auth.login_required
    def get(id):
        user = User.objects(user_id=id).first()
        if user == None:
            return jsonify({'Result':'User does not exist'})
        return user.to_json()

    @user_view.route('/users/<id>', methods=['PUT'])
    @auth.login_required
    def put(id):
        if not request.json:
            abort(400)
        user = User.objects(user_id=id)
        if user.first() == None:
            return jsonify({'Result':'User does not exist'})
        if 'cliqs' in request.json:
            user.update(cliqs, request.json['cliqs'])
        if 'first_name' in request.json:
            user.update(first_name, request.json['first_name'])
        if 'last_name' in request.json:
            user.update(last_name, request.json['last_name'])
        if 'gender' in request.json:
            user.update(gender=request.json['gender'])
        if 'phone' in request.json:
            user.update(phone, request.json['phone'])
        if 'age' in request.json:
            user.update(age, request.json['age'])
        return user.first().to_json()

    @user_view.route('/users/<id>', methods=['DELETE'])
    @auth.login_required
    def delete(id):
        user = User.objects(user_id=id)
        if user.first() == None:
            return jsonify({'Result':'User does not exist'})
        user.delete()
        return jsonify({'Result': 'Deleted'})

user_view.add_url_rule('/users/', view_func=UserView.as_view('users'))
