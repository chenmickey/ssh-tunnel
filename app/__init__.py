from flask import Flask


def create_app(ConfigClass):
	app = Flask(__name__)
	app.config.from_object(ConfigClass)
	return app
