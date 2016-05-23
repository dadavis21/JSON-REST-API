from flask import Flask, jsonify
from flask.ext.mongoengine import MongoEngine
import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from base64 import b64encode
import json
from json_rest_api import app
from cliq import Cliq
from user import User

class viewTestCase(unittest.TestCase):

    def setUp(self):
        app.config['MONGO_DB'] = 'test_db'
        app.config['TESTING'] = True
        self.app = app.test_client()
        db = MongoEngine(app)

    def tearDown(self):
        Cliq.drop_collection()
        User.objects.delete()

    def test_empty_db(self):
        header = {'Authorization': 'Basic ' + b64encode("{0}:{1}".format('admin', 'secret'))}
        rv = self.app.get('/users/"dill"', headers=header)
        rv = json.loads(rv.data)
        self.assertEqual("User does not exist", rv['Result'])
        rv = self.app.get('/cliqs/"group"', headers=header)
        rv = json.loads(rv.data)
        self.assertEqual("Cliq does not exist", rv['Result'])

    def test_rest_user(self):
        header = {'Authorization': 'Basic ' + b64encode("{0}:{1}".format('admin', 'secret'))}

        #Test post
        d = dict(user_id = "Dillon", cliqs=["group"], first_name ="Dillon", last_name ="Davis", gender ="male", phone ="0123456789", age =19)
        rv = self.app.post('/users/', data=json.dumps(d), content_type ='application/json', headers=header)
        rv = json.loads(rv.data)
        self.assertEqual("Dillon", rv['user_id'])
        self.assertEqual(['group'], rv['cliqs'])
        self.assertEqual('Dillon', rv['first_name'])
        self.assertEqual('Davis', rv['last_name'])
        self.assertEqual('male', rv['gender'])
        self.assertEqual('0123456789', rv['phone'])
        self.assertEqual(19, rv['age'])

        #Test get
        rv = self.app.get("/users/'Dillon'", headers=header)
        rv = json.loads(rv.data)
        self.assertEqual("Dillon", rv["user_id"])
        self.assertEqual(['group'], rv["cliqs"])
        self.assertEqual('Dillon', rv["first_name"])
        self.assertEqual('Davis', rv['last_name'])
        self.assertEqual('male', rv['gender'])
        self.assertEqual('0123456789', rv['phone'])
        self.assertEqual(19, rv['age'])

        #Test put
        d = dict(first_name='Dylan')
        rv = self.app.put("/users/'Dillon'", data=json.dumps(d), content_type='application/json', headers=header)
        rv = json.loads(rv.data)
        self.assertEqual('Dylan', rv['first_name'])

        #Test delete
        rv = self.app.delete("/users/'Dillon'", headers=header)
        rv = json.loads(rv.data)
        self.assertEqual('Deleted', rv['Result'])
        rv = self.app.get("/users/'Dillon'", headers=header)
        rv = json.loads(rv.data)
        self.assertEqual('User does not exist', rv['Result'])

    def test_rest_cliq(self):
        header = {'Authorization': 'Basic ' + b64encode("{0}:{1}".format('admin', 'secret'))}

        #Test post
        d = dict(cliq_id='group', members= ['Dillon'], bio='Test cliq', pending_members=['John'])
        rv = self.app.post('/cliqs/', data=json.dumps(d), content_type ='application/json', headers=header)
        rv = json.loads(rv.data)
        self.assertEqual('group', rv['cliq_id'])
        self.assertEqual(['Dillon'], rv['members'])
        self.assertEqual('Test cliq', rv['bio'])
        self.assertEqual(['John'], rv['pending_members'])

        #Test get
        rv = self.app.get('/cliqs/"group"', headers=header)
        rv = json.loads(rv.data)
        self.assertEqual('group', rv['cliq_id'])
        self.assertEqual(['Dillon'], rv['members'])
        self.assertEqual('Test cliq', rv['bio'])
        self.assertEqual(['John'], rv['pending_members'])

        #Test put
        d = dict(bio='New test cliq', headers=header)
        rv = self.app.put("/cliqs/'group'", data=json.dumps(d), content_type='application/json')
        rv = json.loads(rv.data)
        self.assertEqual('New test cliq', rv['bio'])

        #Test delete
        rv = self.app.delete("/cliqs/'group'", headers=header)
        rv = json.loads(rv.data)
        self.assertEqual('Deleted', rv['Result'])
        rv = self.app.get("/cliqs/'group'")
        rv = json.loads(rv.data)
        self.assertEqual('Cliq does not exist', rv['Result'])


if __name__ == '__main__':
    unittest.main()
