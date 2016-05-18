from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

#General configuration for mongodb
app.config["MONGODB_SETTINGS"] = {
    'DB': "json_rest_api"
}
app.config["SECRET_KEY"] = "whoridesmongo"

db = MongoEngine(app)

def register_blueprints(app):
    from views import views
    app.register_blueprint(views)
register_blueprints(app)

if __name__ == '__main__':
    app.run()
