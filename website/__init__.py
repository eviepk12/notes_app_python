from flask import Flask
from flask_sqlalchemy import SQLAlchemyv as db

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jaisdfaadfhasdfhsdf' # secret key that should not be known other than the developers for decrypting data
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}" # locates the sql alchemy database
    db.init_app()

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app