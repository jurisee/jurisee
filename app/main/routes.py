from flask import render_template
from app.main import main_bp
from app.main.forms import RegisterForm

@main_bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@main_bp.route('/about', methods=('GET', 'POST'))
def about():
    return render_template('about.html')

@main_bp.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)