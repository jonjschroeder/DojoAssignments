from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("reg.html")

@app.route('/result',methods=['POST'])
def result():
    email=request.form['email']
    fname=request.form['fname']
    lname=request.form['lname']
    passw=request.form['passw']
    conpass=request.form['conpass']
#    if len(password) < 8:
#        print 'not enough characters'


    test = 0



    if email != EMAIL_REGEX:
        flash('You must enter a name')



    if passw != conpass:
        print 'Passwords do not match'

    if len(passw) < 8:
        test = 1
        print 'Password should be 8 characters or more'

    if len(email) < 1:
        test = 1
        print 'Enter email'

    if len(fname) < 1:
        test = 1
        print 'Enter First Name'

    if len(lname) < 1:
        test = 1
        print 'Enter Lastname'

    if len(passw) < 1:
        test = 1
        print 'Enter Password'

    if len(conpass) < 1:
        test = 1
        print 'Confirm Password'

    if test == 1:
        return redirect('/')
    else:
        return render_template('newhtml.html',email = email, fname = fname, lname = lname, passw = passw, conpass = conpass)





app.run(debug=True)
