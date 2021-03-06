from flask import Blueprint

bp = Blueprint(
    'game',
    __name__,
    template_folder="templates",
    static_folder="static"
)

from app.blueprints.game import routes