from src import db, app, bcrypt
from flask import Flask, render_template, redirect, url_for, flash, request, Blueprint,Response,session, abort, current_app
from flask_login import login_user, logout_user, login_required, current_user, login_manager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from src.services.models import Users, Roles
from src.services.utils import *
from werkzeug.utils import secure_filename
from wtforms.validators import input_required
import re
import os
from src import init_app


login_BP = Blueprint('login_BP', __name__, template_folder='templates',static_folder="static", static_url_path="/src/Login/static/css")

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




@login_BP.route('/')
def index():
    return redirect('acceso-login')

@login_BP.route('/acceso-login', methods= ["GET", "POST"])
def login():
    
    
    if request.method == 'POST':
        
        correo = request.form['Username']
        password = request.form['Password']

        if correo == '' or password == '':
            flash('Porfavor ingresa un Correo y Contraseña','warning')
        else:
            user = Users.query.filter_by(correo=correo).first()
            if user is None:
                flash('Usuario o contraseña incorrectos. Inténtalo de nuevo.', 'warning')
            else:
                
                if not bcrypt.check_password_hash(user.password.encode('utf-8'), password.encode('utf-8')):
                    flash('Usuario o contraseña incorrectos. Inténtalo de nuevo.', 'warning')
                else:
                    
                    session['loggedin'] = True
                    session['id'] = user.id
                    session['name'] = user.nombre
                    session['email'] = user.correo
                    session['rol'] =user.id_rol
                    session['role'] = user.rol.rol
                    if user.profile_picture:
                        session['profile_picture'] = user.profile_picture
                        
                    flash(f'Bienvenido {session['name']}, sesion iniciada correctamente', 'success')
                    if user.id_rol == 1:
                        return redirect(url_for('home_BP.AdminDashboard'))
                    elif user.id_rol == 2:
                        return redirect(url_for('home_BP.IngenieroDashboard'))
                    elif user.id_rol == 3:
                        return redirect(url_for('home_BP.VentasDashboard'))
                    elif user.id_rol == 4:
                        return redirect(url_for('home_BP.InstaladorDashboard'))
                    else:
                        abort(403)  # Acceso prohibido para otros roles
                    
    return render_template('login.html')

@login_BP.route('/Empleados')
def empleados():
    pagina_actual= 'empleados'
    Empleados = Users.query.all()
    return render_template('usercrud.html', Empleados=Empleados, pagina_actual=pagina_actual)

@login_BP.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    pagina_actual= 'empleados'
    # Obtener roles disponibles desde la base de datos
    roles = Roles.query.all()

    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        nombre = request.form['name']
        password = request.form['password']
        correo = request.form['email']
        id_rol = request.form['roles']  # Obtener el rol seleccionado del formulario
        file = request.files['foto']
        cedula = request.form['cedula'] 
        user_exists = Users.query.filter_by(correo=correo).first() is not None

        message = [] 
        
        if file.filename == '':  
            flash('Sube una imagen primero', 'Warning')
            return render_template('useradd.html')
        if file:
            basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
            filename = secure_filename(file.filename) #Nombre original del archivo

            #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
            extension = os.path.splitext(filename)[1]
            nuevoNombreFile = f"{nombre.replace(' ', '_')}_{cedula.replace('-', '_')}"+ extension
            #print(nuevoNombreFile)
        
            upload_path = os.path.join (basepath, app.config['UPLOAD_FOLDER'], nuevoNombreFile) 
            file.save(upload_path)
            
        
        
        if user_exists:
            flash('Este Correo ya existe!', 'Warning')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', correo):
            flash('Correo invalido!', 'Warning')
        elif not nombre or not password or not correo:
            flash('Completa todo el Formulario!', 'Warning')
        elif not id_rol:
            flash('Por Favor, Selecciona un rol!', 'Warning')
        else:
            # Verificar si el id de rol seleccionado existe en la base de datos
            role = Roles.query.get(id_rol)
            if role:
                hashed_password = bcrypt.generate_password_hash(password)
                new_user = Users(correo=correo, password=hashed_password, id_rol=id_rol, nombre=nombre, profile_picture=nuevoNombreFile, cedula = cedula)
                db.session.add(new_user)
                db.session.commit()
                flash('¡Usuario registrado Exitosamente!', 'success')
            else:
                flash('Invalid role selected!', 'warning')

    # Renderizar el formulario de registro con la lista de roles disponibles
    return render_template('useradd.html',  roles=roles, pagina_actual=pagina_actual)

@login_BP.route('/profile', methods=['GET', 'POST'])
def profile():
    user_id = session['id']  # Asumimos que tienes el ID del usuario en la sesión
    user = Users.query.get(user_id)  # Obtén el usuario de la base de datos
    
    if request.method == 'POST':
        name = request.form.get('nombre')
        email = request.form.get('correo')
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        # Handle profile picture update
        if 'profile_picture' in request.files:
            file = request.files['profile_picture']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                old_picture = user.profile_picture
                if old_picture:
                    old_picture_path = os.path.join(app.config['UPLOAD_FOLDER'], old_picture)
                    if os.path.exists(old_picture_path):
                        os.remove(old_picture_path)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                user.profile_picture = filename  # Actualiza la imagen de perfil en la base de datos
                session['profile_picture'] = filename  # Actualiza la imagen de perfil en la sesión

        # Handle name and email update
        if name:
            user.nombre = name  # Actualiza el nombre en la base de datos
            session['name'] = name  # Actualiza el nombre en la sesión
        if email:
            user.correo = email  # Actualiza el correo en la base de datos
            session['email'] = email  # Actualiza el correo en la sesión

        # Handle password update
        if new_password and confirm_password:
            if new_password == confirm_password:
                if bcrypt.check_password_hash(user.password, current_password):
                    new_password_hash = bcrypt.generate_password_hash(new_password).decode('utf-8')
                    user.password = new_password_hash  # Actualiza la contraseña en la base de datos
                    flash('Contraseña actualizada correctamente', 'success')
                else:
                    flash('Contraseña actual incorrecta', 'danger')
            else:
                flash('Las nuevas contraseñas no coinciden', 'danger')

        db.session.commit()  # Guarda los cambios en la base de datos
        return redirect(url_for('login_BP.profile'))

    # Renderizar la plantilla correspondiente según el rol del usuario
    id_rol = user.id_rol
    if id_rol == 1:
        return render_template('user_profile_admin.html', user=user)
    elif id_rol == 2:
        return render_template('user_profile_ingeniero.html', user=user)
    elif id_rol == 3:
        return render_template('user_profile_ventas.html', user=user)
    elif id_rol == 4:
        return render_template('user_profile_instalador.html', user=user)
    else:
        abort(403)  # Acceso prohibido para otros roles
        

@login_BP.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = Users.query.get_or_404(user_id)
    if request.method == 'POST':
        user.nombre = request.form['nombre']
        user.correo = request.form['correo']
        user.cedula = request.form['cedula']
        
        if request.form['password']:
            user.password = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        db.session.commit()
        flash('Usuario actualizado correctamente', 'success')
        return redirect(url_for('login_BP.manage_users'))
    
    return render_template('update_user.html', user=user)

@login_BP.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = Users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('Usuario eliminado correctamente', 'success')
    return redirect(url_for('login_BP.empleados'))

@login_BP.route('/logout')
def logout():
    session.clear()
    flash('La sesión fue cerrada!', 'success')
    return redirect(url_for('login_BP.index'))