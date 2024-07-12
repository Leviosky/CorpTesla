from flask import Flask
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
app = Flask(__name__)
bcrypt = Bcrypt()


def init_app(config):
    app.config.from_object(config)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:corptesla12@localhost:3306/tesla'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'Ctesla12'
    app.config['UPLOAD_FOLDER'] = 'static/img'
    app.config['UPLOAD_COT'] = 'src/DashBoard/static/cot'
    app.config['UPLOAD_FACT'] = 'src/DashBoard/static/fact'
    app.config['UPLOAD_PLAN'] = 'src/DashBoard/static/plan'
    

    
    
    


    bcrypt.init_app(app)
    db.init_app(app)
    migrate = Migrate(app, db)



    # BLUEPRINTS
    from src.Login.login import login_BP
    from src.DashBoard.home import home_BP
    app.register_blueprint(login_BP)
    app.register_blueprint(home_BP)

    return app, db