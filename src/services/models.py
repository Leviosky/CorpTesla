from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from src import db

          
class Users(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True , autoincrement=True)
    correo = db.Column(db.String(100), index=True, unique=True)
    password = db.Column(db.String(100), index=True, unique=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('roles.id_rol'), nullable=False, unique=True)
    nombre = db.Column(db.String(30), index=True, unique=True)
    rol = relationship('Roles', foreign_keys=[id_rol], backref='users')


class Roles(db.Model):
    __tablename__ = "roles"
    id_rol = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rol = db.Column(db.String(20), unique=True)


class Client(db.Model):
    __tablename__="clientes"
    ClientesID = db.Column(db.Integer, primary_key=True , autoincrement=True)
    ClienteNombre = db.Column(db.String(50), index=True, unique=True)
    ClienteCedula = db.Column(db.String(15), index=True, unique=True)
    ClienteTel = db.Column(db.String(15), index=True, unique=True)
    ClienteEmail = db.Column(db.String(50), index=True, unique=True)
    id_services = db.Column(db.Integer, db.ForeignKey('servicios.id_services'))
    ClienteComent = db.Column(db.String(200), index=True, unique=True)
    ClienteLat = db.Column(db.String(100), index=True, unique=True)
    ClienteLon = db.Column(db.String(100), index=True, unique=True)
    ClienteDone = db.Column(db.Boolean, default=False)
    def __init__(self,ClienteNombre,ClienteCedula,ClienteTel,ClienteEmail,id_services,ClienteComent,ClienteLat,ClienteLon):
        self.ClienteNombre = ClienteNombre
        self.ClienteCedula = ClienteCedula
        self.ClienteTel = ClienteTel
        self.ClienteEmail = ClienteEmail
        self.id_services = id_services
        self.ClienteComent = ClienteComent
        self.ClienteLat = ClienteLat
        self.ClienteLon = ClienteLon

    servicio = relationship("Services")

        

class Services(db.Model):
    __tablename__="servicios"
    id_services = db.Column(db.Integer, primary_key=True, autoincrement=True)
    services = db.Column(db.String(100), unique=True)