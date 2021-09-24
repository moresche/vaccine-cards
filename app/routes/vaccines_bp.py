from app.controllers.vaccine_cards_controller import get_vaccine_cards, post_vaccine_cards
from flask import Blueprint

bp = Blueprint('vaccines_bp', __name__, url_prefix='/vaccines')

bp.get('')(get_vaccine_cards)
bp.post('')(post_vaccine_cards)
