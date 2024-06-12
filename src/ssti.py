from jinja2 import Template
from flask import request

import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

PASSWORD = 'j8dsu.8s7kd8saj*saj98'

@app.route('/', methods=['GET'])
def home():
    renderer = Template('Hello, ' + request.args['name'])
    return renderer.render()

app.run()