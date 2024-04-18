from flask import render_template, request, url_for, flash, redirect, session, g, make_response
from app.main import main_bp
from app.extensions import db
from app.main.forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user
from datetime import timedelta

@main_bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@main_bp.route('/about', methods=('GET', 'POST'))
def about():
    return render_template('about.html')

@main_bp.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(
            email=email).first()  # if this returns a user, then the email already exists in database

        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            flash('An account using this email address already exists')
            return redirect(url_for('main.login'))

        # create a new user with the form data. Hash the password so the plaintext version isn't saved.
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256'))

        # add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main_bp.route('/login', methods=('GET', 'POST'))
def login():
    #ADD ERROR HANDLING TO REDIRECT TO PROFILE PAGE IF ALREADY LOGGED IN
    form = LoginForm()
    if current_user.is_authenticated:
         return redirect(url_for('main.profile'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # check if the user actually exists
        user = User.query.filter_by(email=email).first()
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user or not check_password_hash(user.password, password):
            flash('The username or password is incorrect.')
            return redirect(url_for('main.login'))  # if the user doesn't exist or password is wrong, reload the page
        login_user(user)
        session.permanent = True
        session['user'] = user.id
        return redirect(url_for('main.profile'))
    return render_template('login.html', form=form)

@main_bp.route('/profile', methods=('GET', 'POST'))
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main_bp.route('/logout', methods=('GET', 'POST'))
@login_required
def logout():
    logout_user()
    session.pop("user", None)
    return redirect(url_for('main.index'))

@main_bp.route('/codeconduct', methods=('GET', 'POST'))
def codeconduct():
    return render_template('codeconduct.html')