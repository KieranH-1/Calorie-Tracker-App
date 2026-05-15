from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", text="Testing", user="Kieran", boolean=True)

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(email=email).first()
        if user: 
            flash('Email already exists.', category='error')
        elif email.__contains__('@') == False or email.__contains__('.') == False:
            flash('Please enter a valid email address.', category='error')
        elif " " in email:
            flash('Email must not contain spaces.', category='error')
        elif len(email) > 150:
            flash('Email must be less than 150 characters.', category='error')
        elif not is_valid_password(password):
            flash('Please enter a valid password.', category='error')
        elif password != confirm_password:
            flash('Passwords don\'t match.', category='error')   
        elif len(password) > 150:
            flash('Password must be less than 150 characters.', category='error')
        else:
            #add user to database
            new_user = User(email=email, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    
    return render_template("sign_up.html")

def is_valid_password(password):
    if len(password) < 7:
        return False
    if " " in password:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in "!@#$%^&*()_+-=[]{}|;':\"<>,.?/" for char in password):
        return False
    return True