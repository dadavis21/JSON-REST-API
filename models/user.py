from flask import url_for
from json_rest_api import db
import cliq

class User(db.Document):
    user_id = db.StringField(max_length=50, required=True)
    cliqs = db.ListField(ReferenceField('Cliq'), required=True)
    first_name = db.StringField(max_length=50, required=True)
    last_name = db.StringField(max_length=50, required=True)
    gender = db.StringField(required=True)
    phone = db.StringField(required=True)
    age = db.IntField()
    _id = ObjectIdField(unique=True, required=True)