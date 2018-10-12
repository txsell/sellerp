import sys
sys.path.append("../..")
from sellerpapp.mainApp import app, db
from sellerpapp.models import User, Document, Project
from flask_script import Manager, prompt_bool
import requests
import sys

manager = Manager(app)

@manager.command
def initdb():
	db.create_all()
	db.session.add(User(email="archiejain1021@gmail.com", firstName="Arnav", lastName="Jain", password_hash="randompassword", position="Director", department="Technology", year="Senior", number="5033141890", attendance=0))
	db.session.commit()
	print('Initialized the database.')

@manager.command
def dropdb():
	if prompt_bool(
		"Are you sure you want to lose all you data?"):
		db.drop_all()
		print('Dropped the database.')

if __name__ == '__main__':
	manager.run()

