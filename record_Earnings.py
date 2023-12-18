from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user
from .models import Product_Earnings, db
from datetime import datetime

earnings_bp = Blueprint('earnings', __name__, url_prefix='/Earnings')

@earnings_bp.route('/record_earnings', methods=['GET', 'POST'])
def record_earnings():
    user=current_user
    if request.method == 'POST':
        # Retrieve form data
        product_name = request.form.get('product_name')
        earnings_amount = request.form.get('earnings_amount')

        try:
            # Convert earnings_amount to float
            earnings_amount = float(earnings_amount)

            # Create a new Product_Earnings instance
            new_earning = Product_Earnings(
                product_name=product_name,
                earnings_amount=earnings_amount,
            )

            # Add the new earning to the database
            db.session.add(new_earning)
            db.session.commit()

            flash('Earnings recorded successfully!', 'success')
        except ValueError as e:
            flash(f"Error recording earnings: {e}", 'error')

    return render_template('record_earnings.html', user=user)