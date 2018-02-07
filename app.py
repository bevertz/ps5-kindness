from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def homepage():
    eastern = pytz.timezone('US/Eastern')
    nyc_datetime = datetime.now(eastern)
    the_time = nyc_datetime.strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <h1>Welcome to our group dogooders!</h1>
    <p>It is currently {time}.</p>
    """.format(time=the_time)


@app.route('/sign-up')
def sign_up():
    return render_template('base.html')

@app.route('/login')
def login():
    return render_template('base.html')

@app.route('/check-in')
def check_in():
    return render_template('base.html')

@app.route('/share')
def share():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
