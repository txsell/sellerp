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
	print('Initialized the database.')

@manager.command
def dropdb():
	if prompt_bool(
		"Are you sure you want to lose all you data?"):
		db.drop_all()
		print('Dropped the database.')

# prints titles of all projects
@manager.command
def printprojects():
	print('Projects List:\n')
	for project in Project.query.all():
		print(str(project.title) + ' - ' + str(project.description))
	print('')
if __name__ == '__main__':
	manager.run()
