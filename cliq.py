from flask import url_for
from json_rest_api import db
import datetime

#members and pending_members fields hold user_id fields of users
class Cliq(db.Document):
    cliq_id = db.StringField(max_length=50, required=True)
    members = db.ListField(db.StringField(max_length=50, required=True), required=True)
    bio = db.StringField(max_length=255)
    pending_members = db.ListField(db.StringField(max_length=50))
    last_active = db.DateTimeField(default=datetime.datetime.now)
    _id = db.ObjectIdField(unique=True, required=True)
