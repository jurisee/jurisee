from flask import Blueprint

bp = Blueprint('claims', __name__)

from app.claims import routes