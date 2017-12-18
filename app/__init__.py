from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
from config import config
from flask_login import LoginManager

#from flask_sqlalchemy import SQLAlchemy
#from flask_pymongo import PyMongo

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
#db = SQLAlchemy()
#mongo = PyMongo()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    '''
    app.config.update(
    MONGO_URI='mongodb://localhost:27017/netease',
    MONGO_TEST_URI='mongodb://localhost:27017/test'
    )
    '''
    #app.config['MONGO_DBNAME'] = 'netease'
    
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    #db.init_app(app)
    #mongo.init_app(app)
    login_manager.init_app(app)

    # attach routes and custom error pages here

    from main import main as main_blueprint
    from auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app