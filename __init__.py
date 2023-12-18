from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .products import product_bp
    from .inventory import inventory_bp
    from .add_inventory import add_inventory_bp
    from .Earnings import Earnings_bp
    from .record_Earnings import earnings_bp
    from .Profile import Profile_bp
    from .Change_password import password_bp


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(inventory_bp, url_prefix='/inventory')
    app.register_blueprint(add_inventory_bp, url_prefix='/add_inventory')
    app.register_blueprint(Earnings_bp, url_prefix='/earnings')
    app.register_blueprint(earnings_bp, url_prefix='/Earnings')
    app.register_blueprint(Profile_bp, url_prefix='/profile')
    app.register_blueprint(password_bp, url_prefix='/password')
    

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        from .models import User
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

    db.init_app(app)

