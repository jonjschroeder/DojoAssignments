from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '54321abcde'

def counting():
    if session['counter']:
        session['counter'] += 1
    else:
        session['counter'] = 1

@app.route('/')
def index():
    counting()
    return render_template("index.html")

#    return render_template('index.html')
#    try:
#        session['counter'] += 1
#    except KeyError: # if variable not initialized, this error will appear
#        session['counter'] = 1

@app.route('/', methods=['POST'])
def whenclick():
    if request.form['button'] == "add":
        session['counter'] +=2
    elif request.form['button'] =="clear":
        session['counter'] = 0
#    return redirect('/')
    return render_template('index.html')

#@app.route('/', methods=['POST'])
#def counter():
#    session['num'] += 1
#    return render_template('index.html', num = session['num'])
app.run(debug=True)


#Ninja Level 1
#Add a +2 button underneath the counter that reloads the page and increments counter by 2. Add another route to handle this functionality.

#Ninja Level 2
#Add a reset button that resets the counter back to 1. Add another route to handle this functionality.
