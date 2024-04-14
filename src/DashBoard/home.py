from flask import Blueprint, render_template,request,flash, session, redirect, url_for, abort
from src.services import check_user_role
from src.services.models import Users, Roles, Client
from src.Login import login
from src import db
import re



home_BP = Blueprint('home_BP', __name__, template_folder='templates',static_folder="static",static_url_path="/src/DashBoard/static/css")



@home_BP.route('/Admin/home')
@check_user_role(required_role=1)
def AdminDashboard():
    return render_template('home_admin.html')


@home_BP.route('/clientes/registro', methods=['GET', 'POST'])
def AddClient():
    if request.method == 'POST':
        # Obtén los datos del formulario
        ClienteNombre = request.form['nombre']
        ClienteCedula = request.form['cedula']
        ClienteEmail = request.form['correo']
        ClienteTel = request.form['telefono']
        id_services = request.form['servicio']
        ClienteComent = request.form['comentarios']
        ClienteLat = request.form['latitud']
        ClienteLon = request.form['longitud']
        origin_page = request.form.get('origin_page')
        
        messages_to_flash = [] 
        
        # Verifica si el cliente ya existe en la base de datos
        cliente_existente_cedula = Client.query.filter_by(ClienteCedula=ClienteCedula).first()
        cliente_existente_email = Client.query.filter_by(ClienteEmail=ClienteEmail).first()
        
        if cliente_existente_cedula:
            messages_to_flash.append(('Ya existe un CLIENTE registrado con esta CÉDULA', 'warning'))
            
        if cliente_existente_email:
            messages_to_flash.append(('Ya existe un CLIENTE registrado con este CORREO ELECTRÓNICO', 'warning'))
            
        if not re.match(r'[^@]+@[^@]+\.[^@]+', ClienteEmail):
            messages_to_flash.append(('Dirección de correo electrónico no válida', 'warning'))
            
        
        if messages_to_flash:
            for message, category in messages_to_flash:
                flash(message, category)
        else:
        # Crea un nuevo objeto Client con los datos del formulario
            nuevo_cliente = Client(ClienteNombre, ClienteCedula, ClienteTel, ClienteEmail, id_services, ClienteComent, ClienteLat, ClienteLon)

        # Agrega y guarda el nuevo cliente en la base de datos
            db.session.add(nuevo_cliente)
            db.session.commit()

            flash('Cliente registrado exitosamente', 'success')
            if origin_page:
                return redirect(url_for('home_BP.' + origin_page))
    
    # Manejo del método GET
    # Determine qué plantilla HTML renderizar basada en el tipo de usuario o rol
    user_role = session.get('rol')  # Obtén el rol del usuario de la sesión
    if user_role == 1:
        return render_template('addclient_admin.html')
    elif user_role == 2:
        return render_template('addclient_ingeniero.html')
    elif user_role == 3:
        return render_template('addclient_ventas.html')
    elif user_role == 4:
        return render_template('addclient_instalador.html')
    else:
        abort(403)  # Acceso prohibido si el rol no está definido



@home_BP.route('/Proyectos/Registro')
def AddProject():
    nombre_usuario = login.Datos_usuario['nombre']
    rol_usuario = login.Datos_usuario['rol']  
    if rol_usuario == 1: 
        rol_usuario = 'Admin'
    else: 
        rol_usuario = 'Usuario'
    return render_template('addproject.html', nombre_usuario=nombre_usuario, rol_usuario=rol_usuario)


@home_BP.route('/Proyectos/inspeccion')
def AddInspection():
    nombre_usuario = login.Datos_usuario['nombre']
    rol_usuario = login.Datos_usuario['rol']  
    if rol_usuario == 1: 
        rol_usuario = 'Admin'
    else: 
        rol_usuario = 'Usuario'
    return render_template('addinspection.html', nombre_usuario=nombre_usuario, rol_usuario=rol_usuario)

@home_BP.route('/Proyectos/Tramites')
def AddPaperWork():
    nombre_usuario = login.Datos_usuario['nombre']
    rol_usuario = login.Datos_usuario['rol']  
    if rol_usuario == 1: 
        rol_usuario = 'Admin'
    else: 
        rol_usuario = 'Usuario'
    return render_template('addpaperwork.html', nombre_usuario=nombre_usuario, rol_usuario=rol_usuario)