from dotenv import load_dotenv
from flask import Flask
from os import getenv

load_dotenv()
    
def init_app(app: Flask):
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQL_ALCHEMY_DATABASE_URI")
    app.config['JSON_SORT_KEYS'] = getenv('JSON_SORT_KEYS')
