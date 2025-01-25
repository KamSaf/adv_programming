from src.routes.api import API_ROUTES_BP
from src.routes.api_alt import API_ROUTES_BP as API_ROUTES_BP_ALT
from src.db import create_database


def init_app(app):
    app.register_blueprint(API_ROUTES_BP)
    app.register_blueprint(API_ROUTES_BP_ALT)
    create_database()
