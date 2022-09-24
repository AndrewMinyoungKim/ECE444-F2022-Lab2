import email
from email.message import EmailMessage
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.validators import DataRequired
from wtforms.validators import Email

# To run flask run, run this command:
# $env:FLASK_APP="hello.py"

# Different ways to clear a flask session:
# 1. session.clear()
# 2. [session.pop(key) for key in list(session.keys())]
# 3. [session.pop(key) for key in list(session.keys()) if key != '_flashes']

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string I guess'

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT Email address?',
                        [validators.DataRequired(), validators.Email()])
    # email = StringField('What is your UofT Email address?', validators=[Email()])
    submit = SubmitField('Submit')


@ app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))  # redirect('/')
    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'))


@ app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@ app.errorhandler(404)
def page_not_found(e):
    return '<h1>Uh Oh!</h1>'


@ app.errorhandler(500)
def page_not_found(e):
    return '<h1>Oops, I did it again!</h1>'
