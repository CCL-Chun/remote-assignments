import re
import bcrypt
from app import app
from flask import (request, render_template,
                   redirect, url_for)
from flask_bcrypt import Bcrypt
from . import get_db
bcrypt = Bcrypt(app)

@app.route('/home')
def home():
    """Home page for sign-in or sign-up"""
    return redirect(url_for('sign_in'))

@app.route('/signIn', methods=['GET','POST'])
def sign_in():
    """Sign-in page"""
    msg = ''
    if (request.method == 'POST' and
        all(needs in request.form
            for needs in ['email','password'])):
        elements = ['email', 'password']
        email, password = map(request.form.get, elements)
        cursor = get_db().cursor()
        cursor.execute('SELECT * FROM user WHERE email = %s',(email,))
        account = cursor.fetchone()
        if account:
            if bcrypt.check_password_hash(account['password'], password):
                #check_password_hash() for hashed password check
                msg = f"Welecome back! We miss you, {account['name']}!"
                return render_template('knownuser.html',msg=msg)
            msg = "Incorrect password!"
            return render_template('sign_in.html',msg=msg) #try again
        #redirect to sign up page if found no email address (account = None)
        msg = "E-mail should be Sign-up first!"
        return render_template('sign_up.html',msg=msg)
    return render_template('sign_in.html',msg=msg)

@app.route('/signUp', methods=['GET','POST'])
def sign_up():
    """Sign-up page"""
    msg = ''
    if request.method == 'POST':
        if all(needs in request.form
               for needs in ['email','username','password','age']):
            db = get_db()
            cursor = db.cursor()
            elements = ['email', 'username', 'password', 'age']
            email, username, password, age = map(request.form.get, elements)
            cursor.execute('SELECT * FROM user WHERE email = %s',(email,))
            account = cursor.fetchone()
            if account:
                msg = "This E-mail address has already been registered! Please Sign in here."
                return render_template('sign_in.html',msg=msg)
            elif not re.match(r'^\w[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}',email):
                msg = 'Invalid email address!'
            else:
                hash_passwd = bcrypt.generate_password_hash(password)
                cursor.execute(
                    'INSERT INTO user VALUES (NULL, %s, %s, %s, %s)',
                    (email, hash_passwd, age, username,))
                db.commit() #commit change and save to Database
                msg = f"Hi {username}. You have successfully registered!"
                return render_template('knownuser.html',msg=msg)
        else:
            msg = "Please enter ALL INFO!"
    return render_template('sign_up.html',msg=msg)
