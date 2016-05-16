from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
#General configuration for mongodb
app.config["MONGODB_SETTINGS"] = {
    'DB': "json_rest_api",
    'username': 'api',
    'password': 'cliq'
}
app.config["SECRET_KEY"] = "whoridesmongo"

db = MongoEngine(app)

if __name__ == '__main__'
    app.run()
