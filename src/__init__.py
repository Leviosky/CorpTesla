from flask import Flask, Blueprint
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
bcrypt = Bcrypt()



def init_app(config):
    app.config.from_object(config)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3307/tesla'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'Ctesla12'
    bcrypt.init_app(app)
    db.init_app(app)


    # BLUEPRINTS
    from src.Login.login import login_BP
    from src.DashBoard.home import home_BP
    app.register_blueprint(login_BP)
    app.register_blueprint(home_BP)

    return app, db