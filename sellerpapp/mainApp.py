# coding=utf-8
from __future__ import print_function
import sys, os, operator
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from sellerpapp.models import User, Document, Project
from sellerpapp import db, app, oidc, okta_client
import requests
import json
import smtplib
from itsdangerous import URLSafeTimedSerializer
from sqlalchemy import func
import ntpath
from wtforms import Form, BooleanField, StringField, TextAreaField, DateTimeField, validators
from flask_wtf import Form
from flask_wtf.file import FileField
from werkzeug import secure_filename

basedir = os.path.abspath(os.path.dirname(__file__))

# @app.before_request
# def before_request():
#     if oidc.user_loggedin:
#         g.user = okta_client.get_user(oidc.user_getfield("sub"))
#         found_user = User.get_by_email(g.user.profile.email)
#         # if found_user is not None:
#         #     found_user.firstName = g.user.profile.firstName
#         #     found_user.lastName = g.user.profile.lastName
#         #     found_user.oktaid = g.user.id
#         #     # found_user.position = g.user.profile.userType
#         #     # found_user.department = g.user.profile.department
#         #     # found_user.number = g.user.profile.mobileNumber
#         # elif found_user is None:
#         #     email = g.user.profile.email
#         #     firstName = g.user.profile.firstName
#         #     lastName = g.user.profile.lastName
#         #     oktaid = g.user.id
#         #     # position = g.user.profile.userType
#         #     # department = g.user.profile.department
#         #     # number = g.user.profile.mobileNumber
#         #     new_user = User(email = email, firstName = firstName, lastName = lastName, oktaid = oktaid)
#         #     db.session.add(new_user)
#         db.session.commit()
#     else:
#         g.user = None

# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html")

@app.route("/login")
@oidc.require_login
def login():
    return redirect(url_for(".dashboard"))

@app.route("/logout")
def logout():
    oidc.logout()
    return redirect(url_for(".index"))

@app.route("/dts", methods=['GET', 'POST'])
def dts():
    form = Document()
    if form.validate_on_submit():
        return 'Form Successfully Submitted!'
    return render_template('dts.html', form=form)

# we may want to put this in a separate file that holds all of our form objects
class ProposalForm(Form):
    title = StringField('Title', [validators.Length(max=25), validators.DataRequired()])
    description = TextAreaField('Description', [validators.Length(max=250), validators.DataRequired()])
    link = StringField('Link', [validators.URL(), validators.DataRequired()])
    completion_date = DateTimeField('Completion Date', [validators.DataRequired()], format='%m/%d/%y')
    file = FileField('Timeline', [validators.optional()])

@app.route('/project-proposal', methods=['GET', 'POST'])
@oidc.require_login
def projectproposal():
    form = ProposalForm(request.form)

    if request.method == 'POST' and form.validate():
        # log the time the proposal was created
        created = datetime.now()

        # create project and store it in database
        project = Project(title=form.title.data, description=form.description.data, link=form.link.data, created=created, dueDate=form.completion_date.data)
        db.session.add(project)
        db.session.commit()

        # flash success message
        flash('Project Successfully Submitted', 'success')

        return redirect(url_for('projectproposal'))
    return render_template('project-proposal.html', form=form)

@app.route('/video-chat', methods=['GET', 'POST'])
def test():
    return redirect("https://itshello.co/8btdda")

@app.route("/view-projects/<int:id>", methods=['GET'])
def viewproposal(id):
    project = Project.query.filter_by(id=id).first_or_404()
    return render_template('show_project.html', project=project)

@app.route("/view-projects", methods=['GET'])
def viewproposals():
    return render_template('view-projects-page.html', Projects=Project.query.all())

if __name__ == '__main__':
    app.run(debug=True)
