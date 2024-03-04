from config import Config
from app.extensions import db
from app.extensions import ma
from app.extensions import api
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config.from_object(config_class)

    # Initialize Flask extensions here
db.init_app(app)
Marshmallow(app)
Api(app)

    # Register blueprints here
from app.main import bp as main_bp
app.register_blueprint(main_bp)

from app.news import bp as news_bp
app.register_blueprint(news_bp, url_prefix='/news')

from app.registry import bp as registry_bp
app.register_blueprint(registry_bp, url_prefix='/registry')

from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from app.actions import bp as actions_bp
app.register_blueprint(actions_bp, url_prefix='/actions')

if __name__ == "__main__":
    app.run(host='0.0.0.0')