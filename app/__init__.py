from flask import Flask, render_template

from router.deploy import deploy


def inject_static(app):
	@app.route('/', methods=['get'])
	def index():
		return render_template('index.html')


def create_app(ConfigClass):
	app = Flask(__name__)
	app.config.from_object(ConfigClass)
	app.register_blueprint(deploy, url_prefix='/deploy')
	inject_static(app)
	return app
