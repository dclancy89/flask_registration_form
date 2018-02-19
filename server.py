from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'jklfdsau932hifowehj890fp23yqhoipwhowpgurhtop423ub23y80tp054hgoer'

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/register', methods=['post'])
def register():

	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['email'] = request.form['email']
	session['password'] = request.form['password']
	session['confirm_password'] = request.form['confirm_password']

	first_name_valid = False
	last_name_valid = False
	email_valid = False
	password_valid = True
	confirm_password_valid = True

	#validate first name
	if len(session['first_name']) > 0 and session['first_name'].isalpha():
		first_name_valid = True
	else:
		if len(session['first_name']) < 1:
			flash(u'First Name cannot be blank', 'error')
		if not session['first_name'].isalpha():
			flash(u'First Name must only be letters', 'error')

	#validate last name
	if len(session['last_name']) > 0 and session['last_name'].isalpha():
		last_name_valid = True
	else:
		if len(session['last_name']) < 1:
			flash(u'Last Name cannot be blank', 'error')
		if not session['last_name'].isalpha():
			flash(u'Last Name must only be letters', 'error')

	#validate email
	if len(session['email']) > 0 and EMAIL_REGEX.match(session['email']):
		email_valid = True
	else:
		if len(session['email']) < 1:
			flash(u'Email cannot be blank', 'error')
		if not EMAIL_REGEX.match(session['email']):
			flash(u'Enter a valid email address', 'error')

	if first_name_valid and last_name_valid and email_valid and password_valid and confirm_password_valid:
		session.clear()
		flash(u'Thanks for submitting your information', 'success')


	return redirect('/')

app.run(debug=True)


