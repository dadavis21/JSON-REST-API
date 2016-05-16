from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from JSON-REST-API.models import User, Cliq

class UserView(MethodView):

    def post(self, user):
        db.users.insert(user)

    def get(self, id):
        return db.users.findOne({user_id:id})

    def put(self, id, field, update):
        db.users.update(
            {user_id:id},
            {
                $set: {
                    {field:update}
                }
            }
        )

class CliqView(MethodView):

    def post(self, cliq):
        db.cliqs.insert(cliq)
    def get(self, id):
        return db.cliqs.findOne({cliq_id:id})
    def put(self, id, field, update):
        db.cliqs.update(
            {cliq_id:id},
            {
                $set: {
                    {field:update}
                }
            }
        )
