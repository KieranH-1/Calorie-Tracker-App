from datetime import datetime

from flask import Blueprint, flash, render_template, request
from flask_login import login_required, current_user
from .models import User, Food, UserFood
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        food = request.form.get('food')
        quantity = request.form.get('grams')
        meal = request.form.get('meal')
        date = datetime.strptime(request.form.get('date'), '%Y-%m-%d')

        found_food = Food.query.filter_by(name=food).first()
        if found_food:
            user_food = UserFood(user_id=current_user.id, food_id=found_food.id, quantity=quantity, meal=meal, date=date)
            db.session.add(user_food)
            db.session.commit()
        else:
            flash('Food item not found.', category='error')
    return render_template("home.html", user=current_user)