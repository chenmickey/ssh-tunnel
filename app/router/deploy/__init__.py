from flask import Blueprint

deploy = Blueprint('deploy', url_prefix='/deploy', template_folder='tpls')
