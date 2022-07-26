from flask import Flask

# 2 imports below are for MongoDB setup
from config import Config
from flask_mongoengine import MongoEngine

# import for easy restAPI programming
from flask_restx import Api

api = Api()

app = Flask(__name__)

#for it to work in AWS:
application = app

app.config.from_object(Config)

# mongo db config strin
app.config['MONGODB_SETTINGS'] = {
    'db': 'UTA_Enrollment',
    'host': 'ec2-44-204-180-248.compute-1.amazonaws.com',
    'port': 27017,
    'username':'academydemo',
    'password':'Ac@demy1234'
}

db = MongoEngine()
db.init_app(app)

# initialize api variable
# api.init_app(app)


from application import routes