from src.routes.api import API_ROUTES_BP
from src.queue.db import create_database


def init_app(app):
    app.register_blueprint(API_ROUTES_BP)
    create_database()
