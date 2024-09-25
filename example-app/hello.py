from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

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

if __name__ == '__main__':
    app.run(debug=True)
