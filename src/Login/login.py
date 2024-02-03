
import sys
from flask import Flask, render_template, redirect, url_for, flash, request, Blueprint,Response,session,flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_mysqldb import MySQL

#sys.path.insert(1
from src.database.Conexion import *
login_BP = Blueprint('login_BP', __name__, template_folder='templates',static_folder="static", static_url_path="/src/Login/static/css")

Datos_usuario = {}

@login_BP.route('/')
def index():
    return redirect('acceso-login')

@login_BP.route('/acceso-login', methods= ["GET", "POST"])
def login():
    if request.method == 'POST' and 'Username' in request.form and 'Password' in request.form:
        
        _correo = request.form['Username']
        _password = request.form['Password']

        cone = CConexion.ConexionBaseDeDatos()
        cur = cone.cursor()
        cur.execute('SELECT * FROM usuarios WHERE correo = %s AND password = %s', (_correo, _password,))
        account = cur.fetchone()
        cur.close()
        print(account)
        if account:
            session['logueado'] = True
            session['id'] = account[0]
            session['id_rol'] = account[3]
            session['nombre'] = account[4]
            
            Datos_usuario['nombre']= session['nombre']
            Datos_usuario['rol'] = session['id_rol']
        if session['id_rol'] == 1:
            
            return redirect(url_for('home_BP.home'))
        elif session['id_rol'] == 2:
            
            return redirect(url_for('home_BP.home'))
    else:
        return render_template('login.html', mensaje="Usuario o Contraseña Incorrectos")

