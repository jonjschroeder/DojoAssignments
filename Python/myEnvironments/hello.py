from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/projects')
def projectlist():
    return "List"
@app.route('/about')
def about():
    return render_template('index1.html')


app.run(debug=True)
