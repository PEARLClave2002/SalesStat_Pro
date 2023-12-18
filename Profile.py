from flask import Blueprint, render_template, request
from flask import render_template, url_for
from flask_login import login_required, current_user

Profile_bp = Blueprint('profile', __name__, url_prefix='/profile')
@Profile_bp.route('/profile')
def Profile():
    user = current_user
    return render_template('Profile.html', user=user)
