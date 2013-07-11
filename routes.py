from flask import *

app=Flask(__name__)
 
@app.route('/')
def index():
	return render_template('home.html')
 
@app.route('/welcome')
def welcome():
 	return render_template('welcome.html')

@app.route('/hello')
def hello():
	return render_template('hello.html')

@app.route('/Login',methods=['GET','POST'])
def login():
	error=None
	if request.method=='POST':
		if request.form['username']!='admin' or request.form['password']!='admin':
			error="The Username or Password you entered is Invalid!"
		else:
			return redirect(url_for('hello'))
	return render_template('login.html',error=error)

if __name__=='__main__':
	app.run(debug=True)
