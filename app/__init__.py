from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():

        from app.models

    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix="/api/users")

    return app
