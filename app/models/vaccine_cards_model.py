from app.exceptions.vaccine_cards import InvalidCPFError
from sqlalchemy.orm import validates
from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime


@dataclass
class VaccineCard(db.Model):
    cpf: str
    name: str
    first_shot_date: datetime
    second_shot_date: datetime
    vaccine_name: str
    health_unit_name: str
    
    __tablename__ = 'vaccine_card'

    cpf = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    first_shot_date = db.Column(db.DateTime)
    second_shot_date = db.Column(db.DateTime)
    vaccine_name = db.Column(db.String, nullable=False)
    health_unit_name = db.Column(db.String)

    @validates('cpf')
    def validate_cpf(self, key, cpf):
        if type(cpf) != str or len(cpf) != 11:
            raise InvalidCPFError
        return cpf