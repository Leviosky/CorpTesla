from flask import Flask, Blueprint
from config import DevelopmentConfig
from flask_mysqldb import MySQL
from flask_login import LoginManager
from src.Login.login import login_BP
from src.DashBoard.home import home_BP
import mysql.connector 
import os




app = Flask(__name__,)

def init_app(config):
    app.config.from_object(config)
    #BLUEPRINTS
    app.register_blueprint(login_BP)
    app.register_blueprint(home_BP)
    
    return app


