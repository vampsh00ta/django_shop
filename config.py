from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
#иницилиазация приложения
app = Flask(__name__)

#login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.secret_key = 'lilpenis'

#заголовки
CORS(app)

#база данных
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///goods.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sad'
app.config['EXTEND_EXISTING'] = True


#admin

admin  = Admin(app)






