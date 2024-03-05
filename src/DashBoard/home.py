from flask import Blueprint, render_template,request,flash, session, redirect, url_for
from src.services import check_user_role
from src.services.models import Users, Roles
from src.Login import login



home_BP = Blueprint('home_BP', __name__, template_folder='templates',static_folder="static",static_url_path="/src/DashBoard/static/css")



@home_BP.route('/Admin/home')
@check_user_role(required_role=1)
def AdminDashboard():
    return render_template('index.html')


@home_BP.route('/clientes/registro')
def AddClient():
    
    return render_template('addclient.html')


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