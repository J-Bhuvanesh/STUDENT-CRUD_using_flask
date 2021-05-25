from flask import Flask,request,Response,jsonify
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/student_database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




