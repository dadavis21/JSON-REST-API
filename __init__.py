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
    from userView import user_view
    from cliqView import cliq_view
    app.register_blueprint(user_view)
    app.register_blueprint(cliq_view)
register_blueprints(app)

if __name__ == '__main__':
    app.run()
