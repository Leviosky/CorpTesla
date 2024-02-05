from flask import Blueprint, render_template,request,flash
from src.database import *
from src.Login import login



home_BP = Blueprint('home_BP', __name__, template_folder='templates',static_folder="static",static_url_path="/src/DashBoard/static/css")

@home_BP.route('/home')
def home():
    if login.Datos_usuario:
        nombre_usuario = login.Datos_usuario['nombre']
        rol_usuario = login.Datos_usuario['rol']  
        if rol_usuario == 1: 
            rol_usuario = 'Admin'
        else: 
            rol_usuario = 'Usuario'
        return render_template('index.html', nombre_usuario=nombre_usuario, rol_usuario=rol_usuario)

@home_BP.route('/clientes/registro')
def AddClient():
    nombre_usuario = login.Datos_usuario['nombre']
    rol_usuario = login.Datos_usuario['rol']  
    if rol_usuario == 1: 
        rol_usuario = 'Admin'
    else: 
        rol_usuario = 'Usuario'
    return render_template('addclient.html', nombre_usuario=nombre_usuario, rol_usuario=rol_usuario)


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