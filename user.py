from flask import url_for
from json_rest_api import db
from bson.objectid import ObjectId

#previous_cliqs holds cliq_id's of old cliqs
class User(db.Document):
    user_id = db.StringField(max_length=50, required=True)
    previous_cliqs = db.ListField(db.StringField(max_length=50))
    first_name = db.StringField(max_length=50, required=True)
    last_name = db.StringField(max_length=50, required=True)
    gender = db.StringField(required=True)
    phone = db.StringField(required=True)
    age = db.IntField()
    _id = db.ObjectIdField(unique=True, default=ObjectId())
