from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2
#import re


template_dir = os.path.join(os.path.dirname(__file__), "templates")

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template("form.html")
    return template.render()
   

@app.route("/")
def display():
    template = jinja_env.get_template("form.html")
    return render_template('form.html', user='', password='',
    vpassword='', email='', user_error='', password_error='', 
    verify_error='', email_error='')

@app.route("/", methods=['POST'])
def welcome():

    #user_name = request.form['user']
    user = request.form['user']
    user_password = request.form['password']
    user_verify = request.form['vpassword']
    user_email = request.form['email']

    user_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    
    if user == '':
        user_error = 'That is not a valid username..'
    else:
        user = user
        if len(user) < 3 or len(user) > 20:
            user_error = 'User name must be longer than 3 and shorter than 20 characters.'
        else:
            user = user
            if user:
                for x in user:
                    if x.isspace():
                        user_error = 'User name cannot contain a space.'
                    else:
                        #user = user_name
                        user = user

    if user_password == '':
        password_error = 'Password cannot be blank.'
    else:
        user_password=user_password
        if len(user_password) < 3 or len(user_password) > 20:
            password_error = 'Password must be longer than 3 and shorter than 20 characters.'
            password_error =''
        else:
            user_password=user_password
            if user_password:
                for x in user_password:
                    if x.isspace():
                        password_error = 'Password cannot contain a space.'
                        password_error =''
                    else:
                        user_password=user_password

    if user_verify == '':
        verify_error = 'Passwords do not match.'
        verify_error = ''
    else:
        user_verify=user_verify
        if user_verify != user_password:
            verify_error = 'Password must match.'
            verify_error = ''
        else:
            user_verify=user_verify

    if user_email == '':
        user_email=user_email
    else:
        if '@' not in user_email:
            email_error = 'Missing an "@"'
        elif '.' not in user_email:
            email_error = 'Missing an "."'
        else:
            user_email=user_email
            if len(user_email) < 3 or len(user_email) > 20:
                email_error = 'Email must be longer than 3 and shorter than 20 characters.'
            else:
                user_email=user_email

    if not user_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', name=user)
    else:
        return render_template('form.html', user_error=user_error, password_error=password_error, 
        #verify_error=verify_error, email_error=email_error, user_name=user_name, user_email=user_email)
        verify_error=verify_error, email_error=email_error, user=user, user_email=user_email)

    
             
app.run()