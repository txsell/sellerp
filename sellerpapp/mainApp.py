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

basedir = os.path.abspath(os.path.dirname(__file__))

@app.before_request
def before_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
    else:
        g.user = None

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



if __name__ == '__main__':
    app.run(debug=True)

