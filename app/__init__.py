from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SECRET_KEY'] = 'thisisasimpletutorial'

    db.init_app(app)

    from app.main import mainbp as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')

    return app