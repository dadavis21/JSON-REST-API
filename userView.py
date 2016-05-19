from flask import Blueprint, request, abort, jsonify
from flask.views import MethodView
from user import User
from cliq import Cliq
from bson.objectid import ObjectId
import json

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
        user = User.objects(user_id=id).first()
        if user == None:
            return jsonify({'Result':'User does not exist'})
        return user.to_json()

    @user_view.route('/users/<id>', methods=['PUT'])
    def put(id):
        if not request.json:
            abort(400)
        user = User.objects(user_id=id).first()
        if user == None:
            return jsonify({'Result':'User does not exist'})
        if 'previous_cliqs' in request.json:
            user.update(previous_cliqs, request.json['previous_cliqs'])
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
        return user.to_json()

    @user_view.route('/users/<id>', methods=['DELETE'])
    def delete(id):
        user = User.objects(user_id=id).first()
        if user == None:
            return jsonify({'Result':'User does not exist'})
        user.delete()
        return jsonify ({'Result': 'Deleted'})

user_view.add_url_rule('/users/', view_func=UserView.as_view('users'))
