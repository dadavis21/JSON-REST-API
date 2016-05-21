from flask import Blueprint, request, abort, jsonify
from flask.views import MethodView
from cliq import Cliq
from bson.objectid import ObjectId
from auth import auth
import json
import datetime

cliq_view = Blueprint('cliq_view', __name__)

class CliqView(MethodView):
    @auth.login_required
    def post(self):
        if not request.json:
            abort(400)
        cliq = Cliq.objects(cliq_id=request.json['cliq_id'])
        if cliq.first() != None:
            return jsonify({"Result":"Cliq ID already exists"})
        cliq = Cliq (
            cliq_id = request.json['cliq_id'],
            members = request.json['members'],
            bio = request.json['bio'],
            pending_members = request.json['pending_members'],
            last_active = datetime.datetime.now,
            _id = ObjectId()
        )
        cliq.save()
        return cliq.to_json()

    @cliq_view.route('/cliqs/<id>', methods=['GET'])
    @auth.login_required
    def get(id):
        cliq = Cliq.objects(cliq_id=id).first()
        if cliq == None:
            return jsonify({'Result':'Cliq does not exist'})
        return cliq.to_json()

    @cliq_view.route('/cliqs/<id>', methods=['PUT'])
    @auth.login_required
    def put(id):
        if not request.json:
            abort(400)
        cliq = Cliq.objects(cliq_id=id).first()
        if cliq == None:
            return jsonify({'Result':'Cliq does not exist'})
        if 'members' in request.json:
            cliq.members = request.json['members']
        if 'bio' in request.json:
            cliq.bio = request.json['bio']
        if 'pending_members' in request.json:
            cliq.pending_members = request.json['pending_members']
        if 'last_active' in request.json:
            cliq.last_active = request.json['last_active']
        cliq.save()
        return cliq.to_json()

    @cliq_view.route('/cliqs/<id>', methods=['DELETE'])
    @auth.login_required
    def delete(id):
        cliq = Cliq.objects(cliq_id=id)
        if cliq.first() == None:
            return jsonify({'Result':'Cliq does not exist'})
        cliq.delete()
        return jsonify({'Result':'Deleted'})

cliq_view.add_url_rule('/cliqs/', view_func=CliqView.as_view('cliqs'))
