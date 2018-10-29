from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2



template_dir = os.path.join(os.path.dirname(__file__), "templates")

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template("signup_form.html")
    return template.render()
   

@app.route("/")
def display():
    template = jinja_env.get_template("signup_form.html")
    #template = jinja_env.get_template("form.html")
    return render_template('signup_form.html', user_name='', user_password='',
    #return render_template('form.html', username='', password='',
    vpassword='', user_email='', user_error='', password_error='', 
    verify_error='', email_error='')

@app.route("/", methods=['POST'])
def welcome():

    user_name = request.form['user_name']
    user_password = request.form['user_password']
    user_verify = request.form['user_verify']
    user_email = request.form['user_email']

    user_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    
    if user_name == '':
        user_error = 'That is not a valid username..'
    elif len(user_name) < 3 or len(user_name) > 20:
        user_error = 'User name must be longer than 3 and shorter than 20 characters.'

    if user_password == '':
        password_error = 'Password cannot be blank.'
    elif len(user_password) < 3 or len(user_password) > 20:
        password_error = 'Password must be longer than 3 and shorter than 20 characters.'
    if user_verify == '':
        verify_error = 'Password cannot be blank.'
        #verify_error = '' 
    else: 
        if user_password != user_verify:        
            verify_error = 'Passwords do not match.'
            #verify_error = ''

    
    
    
    #email is optional
    if user_email == '':
        user_email=user_email
    elif '@' not in user_email:
        email_error = 'Missing an "@"'
    elif '.' not in user_email:
        email_error = 'Missing an "."'
    elif len(user_email) < 3 or len(user_email) > 20:
        email_error = 'Email must be longer than 3 and shorter than 20 characters.'
    else:
        user_email=user_email
           
    if not user_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', name=user_name)
    else:
        return render_template('signup_form.html', user_error=user_error, password_error=password_error, 
        verify_error=verify_error, email_error=email_error, user_name=user_name, user_email=user_email)

    
             
app.run()

        