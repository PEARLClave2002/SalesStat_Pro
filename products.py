from flask import Blueprint, render_template
from .models import User
from flask_login import current_user, login_required

product_bp = Blueprint('products', __name__, url_prefix='/products')
@product_bp.route('/products')
def products():
    user = current_user
    return render_template('products.html', user=user)