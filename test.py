from flask import Flask, flash, redirect, render_template, request, session, url_for, jsonify, send_file
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.binary import Binary
import uuid, json, io
import hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl, smtplib, hashlib, uuid
from werkzeug.utils import secure_filename

import os
import datetime as dt
from datetime import datetime, timedelta
app = Flask(__name__)

app.secret_key = "KrrrzPPghtfgSKbtJEQCTA"
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.permanent_session_lifetime = timedelta(minutes=15)

client = MongoClient("mongodb+srv://21z233:vitalink@db.rj56s.mongodb.net/?retryWrites=true&w=majority&appName=db")
db = client["db"]


#-----------FUNCTIONS-----------------

def addDoctor(cat, id, name, password):
    password.replace("\n", "")
    passHash = hashlib.sha512(password.encode('utf-8')).hexdigest()
    doctor = {'type': "Doctor", 'category': cat, 'ID': id, 'fullName': name, 'PassHash': passHash, "PFP":"/static/images/empty_user.jpg","patients":[]}
    db["dataset"].insert_one(doctor)
    return doctor

def addIT(id, name, password):
    password.replace("\n", "")
    passHash = hashlib.sha512(password.encode('utf-8')).hexdigest()
    doctor = {'type': "IT", "category":"IT", 'ID': id, 'fullName': name, 'PassHash': passHash, "PFP":"/static/images/empty_user.jpg"}
    db["dataset"].insert_one(doctor)
    return doctor

print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello worldddddd")

addIT("IT00001", "Navanee", "Password")