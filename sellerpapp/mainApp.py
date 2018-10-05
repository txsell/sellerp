from __future__ import print_function
import sys, os, operator
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from sellerpapp.models import User, Document, Project
from sellerpapp import db, app
import requests
import json
import smtplib
from itsdangerous import URLSafeTimedSerializer
from sqlalchemy import func 
import ntpath

basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/', methods=['GET', 'POST'])
def index():
	return 'Hello world!'


if __name__ == '__main__':
    app.run(debug=True)

