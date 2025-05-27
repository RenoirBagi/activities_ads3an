from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atividades.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
db = SQLAlchemy(app)