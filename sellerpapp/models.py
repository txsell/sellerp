from datetime import datetime
from sellerpapp import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
import json
import requests
from flask_security import RoleMixin

document_identifier = db.Table('document_identifier',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
	db.Column('document_id', db.Integer, db.ForeignKey('document.id'))
)

project_identifier = db.Table('project_identifier',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
	db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String, unique=True)
	firstName = db.Column(db.String(80))
	lastName = db.Column(db.String(80))
	oktaid = db.Column(db.String)
	# position = db.Column(db.String(80))
	# department = db.Column(db.String(80))
	# year = db.Column(db.String(60))
	# number = db.Column(db.String(12))
	attendance = db.Column(db.Integer)

	@staticmethod
	def get_by_email(email):
		return User.query.filter_by(email=email).first()

	def __repr__(self):
		return "<User: '{}'>".format(self.email)

class Document(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	link = db.Column(db.String)
	title = db.Column(db.String)
	date = db.Column(db.DateTime)
	owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	uniquecode = db.Column(db.String)

	def __repr__(self):
		return "<Document: '{}'>".format(self.title)

class Project(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String)
	description = db.Column(db.String)
	link = db.Column(db.String)
	created = db.Column(db.DateTime)
	dueDate = db.Column(db.DateTime)
	closed = db.Column(db.DateTime)
	creator = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return "<Project: '{}'>".format(self.title)
