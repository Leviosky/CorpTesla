from src import db, app, bcrypt
from flask import Flask, render_template, redirect, url_for, flash, request, Blueprint,Response,session, abort
from flask_login import login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from src.services.models import Users, Roles
import re


login_BP = Blueprint('login_BP', __name__, template_folder='templates',static_folder="static", static_url_path="/src/Login/static/css")



Datos_usuario = {}

@login_BP.route('/')
def index():
    return redirect('acceso-login')

@login_BP.route('/acceso-login', methods= ["GET", "POST"])
def login():
    
    message = ''
    if request.method == 'POST':
        
        correo = request.form['Username']
        password = request.form['Password']

        if correo == '' or password == '':
            message = 'Porfavor ingresa un Correo y Contraseña'
        else:
            user = Users.query.filter_by(correo=correo).first()
            if user is None:
                message = 'Usuario o contraseña incorrectos. Inténtalo de nuevo.'
            else:
                
                if not bcrypt.check_password_hash(user.password.encode('utf-8'), password.encode('utf-8')):
                    message = 'Usuario o contraseña incorrectos. Inténtalo de nuevo.'
                else:
                    
                    session['loggedin'] = True
                    session['id'] = user.id
                    session['name'] = user.nombre
                    session['email'] = user.correo
                    session['rol'] =user.id_rol
                    message = 'Inicio de sesión exitoso!'
                    if user.id_rol == 1:
                        return redirect(url_for('home_BP.AdminDashboard'))
                    elif user.id_rol == 2:
                        return redirect(url_for('home_BP.home_usuario'))
                    else:
                        abort(403)  # Acceso prohibido para otros roles
                    
    return render_template('login.html', message = message)


@login_BP.route('/register', methods=['GET', 'POST'])
def register():
    message = ''

    # Obtener roles disponibles desde la base de datos
    roles = Roles.query.all()

    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        fullname = request.form['name']
        password = request.form['password']
        email = request.form['email']
        selected_role = request.form['role']  # Obtener el rol seleccionado del formulario

        user_exists = Users.query.filter_by(email=email).first() is not None

        if user_exists:
            message = 'Email already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'Invalid email address!'
        elif not fullname or not password or not email:
            message = 'Please fill out the form!'
        elif not selected_role:
            message = 'Please select a role!'
        else:
            # Verificar si el id de rol seleccionado existe en la base de datos
            role = Roles.query.get(selected_role)
            if role:
                hashed_password = bcrypt.generate_password_hash(password)
                new_user = Users(correo=email, password=hashed_password, id_rol=selected_role, nombre=fullname)
                db.session.add(new_user)
                db.session.commit()
                message = 'You have successfully registered!'
            else:
                message = 'Invalid role selected!'

    # Renderizar el formulario de registro con la lista de roles disponibles
    return render_template('register.html', message=message, roles=roles)

@login_BP.route('/logout')
def logout():
        session.clear()
        return redirect(url_for('acceso-login'))
