from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import current_user
from .models import Product_Earnings , db 
from datetime import datetime, timedelta
from flask import current_app

Earnings_bp = Blueprint('Earnings', __name__, url_prefix='/earnings')

@Earnings_bp.route('/earnings', methods=['GET'])
def Earnings():
    user = current_user

    try:
        # Fetch all earnings from the database
        earnings = Product_Earnings.query.all()

        return render_template('earnings.html', user=user, earnings=earnings)
    except Exception as e:
        flash(f"Error fetching earnings: {e}", 'error')

    return render_template('earnings.html', user=user, earnings=[])

@Earnings_bp.route('/search_earnings', methods=['GET'])
def search_earnings():
    user = current_user

    try:
        # Get the search parameter (product name) from the request
        search_product_name = request.args.get('product_name')

        # If a product name is provided, perform a case-insensitive search
        if search_product_name:
            earnings = Product_Earnings.query.filter(Product_Earnings.product_name.ilike(f'%{search_product_name}%')).all()
        else:
            # If no product name is provided, fetch all earnings
            earnings = Product_Earnings.query.all()

        return render_template('earnings.html', user=user, earnings=earnings)
    except Exception as e:
        flash(f"Error fetching earnings: {e}", 'error')

    return render_template('earnings.html', user=user, earnings=[])



