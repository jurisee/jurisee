from flask import render_template
from app.main import bp
from app.extensions import db
from app.main.forms import RegisterForm

@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@bp.route('/about', methods=('GET', 'POST'))
def about():
    return render_template('about.html')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)