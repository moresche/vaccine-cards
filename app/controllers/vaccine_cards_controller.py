from app.exceptions.vaccine_cards import InvalidCPFError
from app.models.vaccine_cards_model import VaccineCard
from flask import jsonify, request, current_app
from datetime import datetime, timedelta

def get_vaccine_cards():
    vaccine_cards = VaccineCard.query.all()
    return jsonify(vaccine_cards), 200

def post_vaccine_cards():
    data = request.json

    data["first_shot_date"] = datetime.now()
    data["second_shot_date"] = data["first_shot_date"] + timedelta(days=90)

    try:
        vaccine_card = VaccineCard(**data)

        session = current_app.db.session

        session.add(vaccine_card)
        session.commit()

        return jsonify(vaccine_card)

    except InvalidCPFError:
        return {"error": "CPF must be a string and contain 11 numeric digits."}, 400
