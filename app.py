from flask import Flask, request, session, redirect, url_for, render_template, flash, request
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html") 
@app.route('/login',methods=['POST'])
def login():
    cofra=[]
    usuario=request.form.get("usuario")
    contraseña=request.form.get("contraseña")
    bd=request.form.get("bd")
    conectar=psycopg2.connect(dbname=bd, user=usuario, password=contraseña, host="localhost")
    cursor=conectar.cursor()
    cursor.execute("SELECT nombrecorto FROM cofradias;")
    cofradias=cursor.fetchall()
    for c in cofradias:
	cofra.append(c)
    return render_template("cofra.html",cofra=cofra)
