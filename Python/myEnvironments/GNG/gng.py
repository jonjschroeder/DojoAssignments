from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = '1'

@app.route('/')
def index():
    if session['random']:
        session['random'] = session['random']
    else:
        session['random'] = random.randint(1,101)

    #session['random'] = random.randint(1,101)
    print session['random']



    return render_template("index.html")



@app.route('/form', methods = ['POST'])
def grabnum():
    guess = int(request.form['number'])
    if guess == session['random']:
        answer = "you got it"
        newbutton = "<input type='submit' value='Play Again!'>"
    elif guess > session['random']:
        answer = "your guess is too high"
    elif guess < session['random']:
        answer = 'your guess is too low'


    print guess
    print type(int(guess))
    print type(session['random'])
    return render_template('index.html', answer1 = answer, newbutton = newbutton)

#@app.route('/form'), methods = ['POST']



app.run(debug=True)
