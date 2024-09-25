from flask import Flask, render_template, session, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

def utoronto_email_check(form, field):
    email = field.data
    if "utoronto" not in email:
        raise ValidationError("Email must contain \"utoronto\".")

class NameForm(FlaskForm):
	name = StringField('What is your name?', validators=[DataRequired("Please add your first and last name.")])
	email = StringField('What is your UofT email?', validators=[DataRequired("Please enter your email"), Email(message="Please include an '@' in the email address"), utoronto_email_check])
	submit = SubmitField('Submit')

@app.route('/')
def home():
	current_time = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")
	return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    # Get the current date and time
    now = datetime.utcnow()
    # Send current time to the template
    return render_template('user.html', name=name, current_time=now)

@app.route('/form/', methods=['GET', 'POST'])
def login(): 
	name = None
	email = None
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		old_email = session.get('email')
		name = form.name.data
		if old_name is not None and old_name != name:
			flash('Looks like you have changed your name!')
		session['name'] = name

		email = form.email.data
		if old_email is not None and old_email != form.email.data:
			flash('Looks like you have changed your email!')
		session['email'] = email

		form.name.data = ''
		form.email.data = ''
	return render_template('form.html', form=form, name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)

