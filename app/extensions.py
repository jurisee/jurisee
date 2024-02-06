
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

db = SQLAlchemy()
ma = Marshmallow()
api = Api()
