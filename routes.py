from flask import *
from functools import wraps

app=Flask(__name__)
 
app.secret_key='Working'
 
@app.route('/')
def index():
	return render_template('home.html')
 
@app.route('/welcome')
def welcome():
 	return render_template('welcome.html')

def login_required(func):
	@wraps(func)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return func(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('login'))
	return wrap

@app.route('/logout')
def logout():
	session.pop('logged_in',None)
	flash("You are now Logged out.")
	return redirect(url_for('login'))

@app.route('/hello')
@login_required
def hello():
	return render_template('hello.html')

@app.route('/Login',methods=['GET','POST'])
def login():
	error=None
	if request.method=='POST':
		if request.form['username']!='admin' or request.form['password']!='admin':
			error="The Username or Password you entered is Invalid!"
		else:
			session['logged_in']=True
			return redirect(url_for('hello'))
	return render_template('login.html',error=error)

if __name__=='__main__':
	app.run(debug=True)
