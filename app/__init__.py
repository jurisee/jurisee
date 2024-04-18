import os
from config import Config
from app.extensions import db
from app.extensions import ma
from app.extensions import api
from flask import Flask
from flask import Blueprint
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
d = os.path.dirname(os.getcwd())
CONFIG_FILE = os.path.join(d, 'jurisee/config.py')
app.config.from_pyfile(CONFIG_FILE)
app.config.from_object(Config)

# Initialize Flask extensions here
db.init_app(app)
login_manager.login_view = 'main.login'
login_manager.init_app(app)
Marshmallow(app)
Api(app)


# Register blueprints here
from app.main import main_bp
app.register_blueprint(main_bp)
from app.news import bp as news_bp
app.register_blueprint(news_bp, url_prefix='/news')
from app.claims import bp as claims_bp
app.register_blueprint(claims_bp, url_prefix='/claims')
from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')
from app.actions import bp as actions_bp
app.register_blueprint(actions_bp, url_prefix='/actions')

