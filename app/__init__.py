from app.configs import env, database, migrations
from app.routes import api_bp
from flask import Flask


def create_app():
    app = Flask(__name__)

    env.init_app(app)
    database.init_app(app)
    migrations.init_app(app)
    app.register_blueprint(api_bp.bp)

    return app