from flask import Flask, render_template, request, session
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
	session.clear()
	session['name']=request.form['name']
	session['location']=request.form['location']
	session['language']=request.form['language']
	session['comment1']=request.form['comment1']
	if len(session['name']) < 1:
		flash('You must enter a name')
	elif len(session['comment1']) < 1:
		flash('You must enter a comment')
	elif len(session['comment1']) > 120:
		flash('comment is too long')
	else:
		return render_template('display.html', name = session['name'], location = session['location'], language = session['language'], comment1 = session['comment1'])

	return redirect('/')


app.run(debug=True) # run our server
