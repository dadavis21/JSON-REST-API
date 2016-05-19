from flask import Blueprint, request, redirect, render_template, url_for, abort
from flask.views import MethodView
from user import User
from cliq import Cliq
from bson.objectid import ObjectId
import json
import datetime
from json_rest_api import db

cliq_view = Blueprint('cliq_view', __name__)

class CliqView(MethodView):

    def post(self):
        if not request.json:
            abort(400)
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

    @cliq_view.route('/cliqs/<id>')
    def get(id):
        cliq = Cliq.objects.get(cliq_id=id)
        return cliq.to_json()

    @cliq_view.route('/cliqs/<id>')
    def put(id):
        cliq = Cliq.objects.get(cliq_id=id)
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
    @cliq_view.route('/cliqs/<id>')
    def delete(id):
        cliq = Cliq.objects.get(cliq_id=id)
        cliq.delete()

cliq_view.add_url_rule('/cliqs/', view_func=CliqView.as_view('cliqs'))
