from flask import render_template
from flask import request
from fondre import fondre
from .form import LoginForm

@fondre.route('/')
@fondre.route('/index/')
def index():
	creator = 'Dayyan Ahmad'
	return render_template('index.html', title='Homepage', creator=creator)

@fondre.route('/login/')
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)

@fondre.route('/')
@fondre.route('/messenger/')
def main():
	return render_template('main.html', username='dossier-hash')


#@fondre.route('/login', method=['POST', 'GET'])