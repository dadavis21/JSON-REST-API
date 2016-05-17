from flask import url_for
from json_rest_api import db
import datetime

class Cliq(db.Document):
    cliq_id = db.StringField(max_length=50, required=True)
    members = db.ListField(ReferenceField('User'), required=True)
    bio = db.StringField(max_length=255)
    pending_members = db.ListField(ReferenceField('User'))
    last_active = db.DateTimeField(default=datetime.datetime.now)
    _id = ObjectIdField(unique=True, required=True)
