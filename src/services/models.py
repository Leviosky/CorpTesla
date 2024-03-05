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