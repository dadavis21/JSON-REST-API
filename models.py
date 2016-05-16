from flask import url_for
from JSON-REST-API import db
import datetime

class User(db.Document):
    user_id = db.StringField(max_length=50, required=True)
    cliqs = db.ListField(ReferenceField('Cliq'), required=True)
    first_name = db.StringField(max_length=50, required=True)
    last_name = db.StringField(max_length=50, required=True)
    gender = db.StringField(required=True)
    phone = db.StringField(required=True)
    age = db.IntField()
    _id = ObjectIdField(unique=True)

class Cliq(db.Document):
    cliq_id = db.StringField(max_length=50, required=True)
    members = db.ListField(ReferenceField('User'), required=True)
    bio = db.StringField(max_length=255)
    pending_members = db.ListField(ReferenceField('User'))
    last_active = db.DateTimeField(default=datetime.datetime.now)
    _id = ObjectIdField(unique=True)
