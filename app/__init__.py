from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    myapp = Flask(__name__)

    from app.controllers.data import data
    myapp.register_blueprint(data, url_prefix='/')

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    db_path = os.path.join(base_dir, 'database', 'database.db')

    if not os.path.exists(os.path.dirname(db_path)):
        os.makedirs(os.path.dirname(db_path))

    myapp.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    myapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(myapp)

    with myapp.app_context():
        db.create_all()

    return myapp
