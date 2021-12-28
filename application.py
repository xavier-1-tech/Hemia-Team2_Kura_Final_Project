from flask import Flask
from flask import render_template, g, redirect, request
from flask.helpers import url_for

# from flask_login import (
#     LoginManager,
#     current_user,
#     login_required,
#     login_user,
#     logout_user,
# )

# from flask_oidc import OpenIDConnect
# from okta.client import Client #as UsersClient

# from flask_login import LoginManager
# from flask_login import login_user

# import okta_jwt_verifier
# #from okta import UserClient

# import json



application = app = Flask(__name__)

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'


#Flask Code
@app.route('/')
def quest():
    return render_template('index.html')

@app.route('/index.html')
def quest10():
    return render_template("index.html")

    

@app.route('/doctor-list.html', methods=['GET', 'POST'])
#@login_required
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