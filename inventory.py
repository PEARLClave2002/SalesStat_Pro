from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import current_user
from .models import Product_Inventory, db  # Assuming your models are in a file named models.py

inventory_bp = Blueprint('inventory', __name__, url_prefix='/inventory')

@inventory_bp.route('/inventory')
def inventory():
    # Fetch product details from the database (assuming you have a Product_Inventory model)
    products = Product_Inventory.query.all()
    user=current_user

    # Render the inventory page and pass the product details to the template
    return render_template('inventory.html',user=user, products=products)

@inventory_bp.route('/edit_inventory/<int:product_id>', methods=['GET', 'POST'])
def edit_inventory(product_id):
    user = current_user
    product = Product_Inventory.query.get(product_id)

    if request.method == 'POST':
        # Retrieve form data for editing
        product_name = request.form.get('product_name')
        quantity_sold = request.form.get('quantity_sold')
        quantity_available = request.form.get('quantity_available')

        try:
            quantity_sold = int(quantity_sold)
            quantity_available = int(quantity_available)

            # Update the existing Product_Inventory instance
            product.product_name = product_name
            product.quantitySold = quantity_sold
            product.quantityAvailable = quantity_available

            # Commit the changes to the database
            db.session.commit()

            flash('Inventory successfully updated!', 'success')
            return redirect(url_for('add_inventory.add_inventory'))
        except ValueError as e:
            flash(f"Error updating inventory: {e}", 'error')

    return render_template('edit_inventory.html', user=user, product=product)

# Add this route to your Flask application
from flask import render_template, redirect, url_for

@inventory_bp.route('/update_quantity/<int:product_id>', methods=['GET', 'POST'])
def update_quantity(product_id):
    product = Product_Inventory.query.get_or_404(product_id)

    if request.method == 'POST':
        try:
            new_quantity_sold = int(request.form['quantity_sold'])
            # Assuming quantityAvailable is a column in your Product_Inventory model
            product.quantityAvailable -= new_quantity_sold
            product.quantitySold += new_quantity_sold

            db.session.commit()
            return redirect(url_for('inventory.inventory'))  # Redirect to inventory page after update
        except ValueError:
            # Handle the case where the input is not a valid integer
            flash('Invalid input for quantity sold. Please enter a valid number.', 'error')

    return render_template('update_quantity.html', product=product)
