from flas import Flask

app = Flask(__name__)
app.route('/')
def dindex():
    return 'Hello World!'

app.run(debug = True)
