from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return "No ninjas here"
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/ninja')
def images():
   return render_template('/disninja1.html')
@app.route('/ninja/<color>')
def choose(color):
    if color == 'purple':
        img = url_for('static', filename='donatello.jpg')
    elif color == 'blue':
        img = url_for('static', filename='leonardo.jpg')
    elif color == 'orange':
        img = url_for('static', filename='michelangelo.jpg')
    elif color == 'red':
        img = url_for('static', filename='raphael.jpg')
    else :
        img = url_for('static', filename='notapril.jpg')
    return render_template('/disninja2.html', img = img)


app.run(debug=True) # run our server
