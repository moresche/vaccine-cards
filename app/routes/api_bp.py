from flask import Blueprint
from . import vaccines_bp

bp = Blueprint('api_bp', __name__, url_prefix='/api')

bp.register_blueprint(vaccines_bp.bp)