from flask import Flask
from flask import render_template, redirect, request
from flask.helpers import url_for

import pytest

import mariadb

import info

#Database
conn = mariadb.connect(
         host= db_host,
         port= db_port,
         user= db_user,
         password= db_password,
         database= db_database)

cur = conn.cursor()

#Application
application = app = Flask(__name__)


@app.route('/')
def quest():
    return render_template('index.html')

@app.route('/index.html')
def quest10():
    return render_template("index.html")


@app.route('/doctor-list.html', methods=['GET', 'POST'])
def quest2():
    return render_template('doctor-list.html')


@app.route('/about.html')
def quest3():
    return render_template('about.html')

@app.route('/lab-add-patient.html')
def quest4():
    return render_template('lab-add-patient.html')

@app.route('/patient-history.html')
def quest5():
    return render_template('patient-history.html')

@app.route('/registration.html')
def quest6():
    return render_template('registration.html')

@app.route('/registration-lab.html')
def quest7():
    return render_template('registration-lab.html')

@app.route('/sign-in-doc.html')
def quest8():
    return render_template('sign-in-doc.html')

@app.route('/sign-in-lab.html')
def quest9():
    return render_template('sign-in-lab.html')


if __name__ == "__main__":
    app.run()
