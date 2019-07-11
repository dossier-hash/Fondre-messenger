from flask import Flask

fondre = Flask(__name__)
fondre.config.from_pyfile('config.py')


from fondre import routes