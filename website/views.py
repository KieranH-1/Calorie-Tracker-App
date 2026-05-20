from flask import Blueprint, flash, render_template, request
from flask_login import login_required, current_user
from .models import User, Food, UserFood

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        food = request.form.get('food')

        found_food = Food.query.filter_by(name=food).first()
        if found_food:
            # Process the submitted food item
            pass
        else:
            # Handle the case where the food item is not found
            flash('Food item not found.', category='error')
    return render_template("home.html", user=current_user)