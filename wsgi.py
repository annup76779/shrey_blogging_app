from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
# initiating SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///./main.db'
app.config["SQLALCHEMY_ECHO"] = True

class User(db.Model):
    __tablename__ = "user_detail"

    id = db.Column(db.Integer,primary_key = True, autoincrement =True)
    email = db.Column(db.String(255), unique = True)
    password = db.Column(db.String(22), nullable=False)
    reg_date_time = db.Column(db.DateTime, nullable=False)

# db.create_all()
# if you have to use the application in console you can use the following command
# from app_name import *
# app.app_context().push()
# after this you can use all the common python command in console for the application

@app.route("/")
def index():
    return jsonify(
        status = True,msg = "I am best at flask"
    )

@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    password = request.form.get("password")

    new_user = User(email = email, password = password, reg_date_time  = datetime.now())

    # adding to the session
    db.session.add(new_user)
    # commiting the change to the database
    db.session.commit()
    return jsonify(status = True, msg="user registered successfully")