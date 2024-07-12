from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from src import db

################################# Usuarios #######################################
class Users(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    correo = db.Column(db.String(100), index=True, unique=True)
    password = db.Column(db.String(100), index=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('roles.id_rol'), nullable=True)
    nombre = db.Column(db.String(30), index=True)
    cedula = db.Column(db.String(30), index=True, unique=True)
    profile_picture = db.Column(db.String(255), nullable=True)
    
    rol = db.relationship('Roles', backref=db.backref('usuarios', lazy=True))


class Roles(db.Model):
    __tablename__ = "roles"
    id_rol = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rol = db.Column(db.String(30), unique=True)

################################ Clientes #######################################
class Client(db.Model):
    __tablename__ = "clientes"
    ClientesID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ClienteNombre = db.Column(db.String(50), index=True)
    ClienteCedula = db.Column(db.String(15), index=True, unique=True)
    ClienteTel = db.Column(db.String(15), index=True)
    ClienteEmail = db.Column(db.String(50), index=True, unique=True)
    id_services = db.Column(db.Integer, db.ForeignKey('servicios.id_services'))
    ClienteComent = db.Column(db.String(200), index=True)
    ClienteLat = db.Column(db.String(100), index=True, unique=True)
    ClienteLon = db.Column(db.String(100), index=True, unique=True)
    ClienteDone = db.Column(db.Boolean, default=False)
    __table_args__ = (db.UniqueConstraint('ClienteCedula', name='ix_clientes_ClienteCedula'),)

    proyectos = relationship("Proyecto", back_populates="cliente")

    servicio = relationship("Services")

    def __init__(self, ClienteNombre, ClienteCedula, ClienteTel, ClienteEmail, id_services, ClienteComent, ClienteLat, ClienteLon):
        self.ClienteNombre = ClienteNombre
        self.ClienteCedula = ClienteCedula
        self.ClienteTel = ClienteTel
        self.ClienteEmail = ClienteEmail
        self.id_services = id_services
        self.ClienteComent = ClienteComent
        self.ClienteLat = ClienteLat
        self.ClienteLon = ClienteLon


class Services(db.Model):
    __tablename__ = "servicios"
    id_services = db.Column(db.Integer, primary_key=True, autoincrement=True)
    services = db.Column(db.String(100), unique=True)

################################ Proyectos #####################################
class ClaseDeProyecto(db.Model):
    __tablename__ = 'clase_de_proyecto'
    ClaseID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Clase = db.Column(db.String(100), nullable=True)


class Proyecto(db.Model):
    __tablename__ = 'proyectos'
    ProjectID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ProjectName = db.Column(db.String(100), nullable=True)
    ClientesID = db.Column(db.Integer, db.ForeignKey('clientes.ClientesID'), nullable=True)
    ClaseID = db.Column(db.Integer, db.ForeignKey('clase_de_proyecto.ClaseID'), nullable=True)
    TipoID = db.Column(db.Integer, db.ForeignKey('servicios.id_services'), nullable=True)
    ProjectLat = db.Column(db.String(100), index=True, unique=True)
    ProjectLon = db.Column(db.String(100), index=True, unique=True)
    InitDate = db.Column(db.Date)
    FinishDate = db.Column(db.Date)
    CompletadoStatus = db.Column(db.Boolean, default=False)
    CanceladoStatus = db.Column(db.Boolean, default=False)

    cliente = relationship('Client', back_populates='proyectos')
    clase_de_proyecto = relationship('ClaseDeProyecto')
    servicio = relationship('Services')

################################ Ventas ########################################
class Propuestas(db.Model):
    __tablename__ = 'propuestas'
    id_propuesta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ProjectID = db.Column(db.Integer, db.ForeignKey('proyectos.ProjectID'), nullable=True)
    Propuesta = db.Column(db.String(255), nullable=True)
    PropuestaFile = db.Column(db.String(255), nullable=True)
    
    proyecto = relationship('Proyecto')


class Ventas(db.Model):
    __tablename__ = 'ventas'
    VentasID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PropuestaID = db.Column(db.Integer, db.ForeignKey('propuestas.id_propuesta'), nullable=True)
    Pago1 = db.Column(db.Boolean, default=False)
    Pago2 = db.Column(db.Boolean, default=False)
    Pago3 = db.Column(db.Boolean, default=False)

############################ Proyecto Solar ###################################
class ProyectoSolar(db.Model):
    __tablename__ = 'proyecto_solar'
    SolarID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    SolarName = db.Column(db.String(255), nullable=True)
    ProjectID = db.Column(db.Integer, db.ForeignKey('proyectos.ProjectID'), nullable=True)
    TechoID = db.Column(db.Integer, db.ForeignKey('tipo_de_techo.id_Techo'), nullable=True)
    TechoInfo = db.Column(db.String(255), nullable=True)
    Aguas = db.Column(db.Integer, nullable=True)
    AreaM2 = db.Column(db.Float, nullable=True)
    IpAmp = db.Column(db.Integer, nullable=True)
    Demanda = db.Column(db.Integer, nullable=True)
    SistemaID = db.Column(db.Integer, db.ForeignKey('sistema_fotovoltaico.id_Sistema'), nullable=True)
    CapacidadInst = db.Column(db.Float, nullable=True)
    PanelID = db.Column(db.Integer, db.ForeignKey('paneles.id_Panel'), nullable=True)
    PanelWatts = db.Column(db.Integer, nullable=True)
    PanelUnits = db.Column(db.Integer, nullable=True)
    BattID = db.Column(db.Integer, db.ForeignKey('bateria.id_Bateria'), nullable=True)
    BattWatts = db.Column(db.Integer, nullable=True)
    BattUnits = db.Column(db.Integer, nullable=True)

    DataLogger = db.Column(db.String(255), nullable=True)
    Medunits = db.Column(db.Integer, nullable=True)
    Medbrand = db.Column(db.String(100), nullable=True)
    Medtipe = db.Column(db.String(100), nullable= True)
    Comentarios = db.Column(db.String(255))

    proyecto = relationship('Proyecto')
    tipo_de_techo = relationship('TipoDeTecho')
    sistema_fotovoltaico = relationship('SistemaFotovoltaico')
    paneles = relationship('Panel')
    bateria = relationship('Bateria')


class Revision(db.Model):
    __tablename__ = 'revision'
    id_revision = db.Column(db.Integer, primary_key=True, autoincrement=True)
    SolarID = db.Column(db.Integer, db.ForeignKey('proyecto_solar.SolarID'), nullable=True)
    PapNaturgy = db.Column(db.Boolean, default=False)
    PapBomberos = db.Column(db.Boolean, default=False)
    PapMunicipio = db.Column(db.Boolean, default=False)
    InversorConfig = db.Column(db.Boolean, default=False)
    InversorLog = db.Column(db.Boolean, default=False)
    letrero = db.Column(db.Boolean, default=False)
    
    proyecto_solar = relationship('ProyectoSolar')

class Diseño(db.Model):
    __tablename__ = 'diseño'
    DiseñoID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    SolarID = db.Column(db.Integer, db.ForeignKey('proyecto_solar.SolarID'), nullable=True)
    Planos = db.Column(db.String(255), nullable=True)
    
    proyecto_solar = relationship('ProyectoSolar')

class TipoDeTecho(db.Model):
    __tablename__ = 'tipo_de_techo'
    id_Techo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Material = db.Column(db.String(100), nullable=True)


class SistemaFotovoltaico(db.Model):
    __tablename__ = 'sistema_fotovoltaico'
    id_Sistema = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Sistema = db.Column(db.String(100), nullable=True)


class Panel(db.Model):
    __tablename__ = 'paneles'
    id_Panel = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Marca = db.Column(db.String(100), nullable=True)

class Bateria(db.Model):
    __tablename__ = 'bateria'
    id_Bateria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Marca = db.Column(db.String(100), nullable=True)

class Inversor(db.Model):
    __tablename__ = 'inversor'
    id_inversor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    SolarID = db.Column(db.Integer, db.ForeignKey('proyecto_solar.SolarID'), nullable=True)
    MarcaID = db.Column(db.Integer, db.ForeignKey('inversores.id_marca'), nullable=True)
    Capacidad = db.Column(db.Integer, nullable=True)
    Model = db.Column(db.String(100), nullable=True)
    
    inversores = relationship('Inversores')
    proyecto_solar = relationship('ProyectoSolar')


class Inversores(db.Model):
    __tablename__ = 'inversores'
    id_marca = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Marca = db.Column(db.String(100))
