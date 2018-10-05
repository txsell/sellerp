import os

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask.ext.security.datastore.sqlalchemy import SQLAlchemyUserDatastore
import smtplib
from flask_login import LoginManager
from flask_mail import Mail

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'sellerp.db')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

app.config['DEBUG'] = False
app.config['SECURITY_RECOVERABLE'] = False
app.config['SECURITY_REGISTERABLE'] = False

app.config['PYTHONHTTPSVERIFY'] = 0

# Configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "index"
login_manager.init_app(app)

db = SQLAlchemy(app)

app.config.update(
	DEBUG=True
	)
