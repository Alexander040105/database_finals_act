# db.py para lang maiwasan yung circular import shit ng python para lang yung magagamit na "db" ng models.py and main.py ay eto na lang bruh
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
