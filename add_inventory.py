from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from .models import Product_Inventory, db

add_inventory_bp = Blueprint('add_inventory', __name__, url_prefix='/add_inventory')

@add_inventory_bp.route('/add_inventory', methods=['GET', 'POST'])
def add_inventory():
    user = current_user
    if request.method == 'POST':
        # Retrieve form data
        product_name = request.form.get('product_name')
        quantity_sold = request.form.get('quantity_sold')
        quantity_available = request.form.get('quantity_available')

        try:
            quantity_sold = int(quantity_sold)
            quantity_available = int(quantity_available)

            # Create a new Product_Inventory instance
            new_product = Product_Inventory(
                product_name=product_name,
                quantitySold=quantity_sold,
                quantityAvailable=quantity_available,
            )

            # Add the new product to the database
            db.session.add(new_product)
            db.session.commit()

            flash('Inventory successfully added!', 'success')
        except ValueError as e:
            flash(f"Error adding inventory: {e}", 'error')

    return render_template('add_inventory.html', user=user)

