from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment

# To run flask run, run this command:
# $env:FLASK_APP="hello.py"

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Uh Oh!</h1>'


@app.errorhandler(500)
def page_not_found(e):
    return '<h1>Oops, I did it again!</h1>'
