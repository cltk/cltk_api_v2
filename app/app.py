""" hello.py """

import json
import os

from flask import Flask, jsonify
from flask_restful import Api
from flask_restful import Resource

app = Flask(__name__)
api = Api(app)

@app.route('/hello')
def hello():
    return jsonify({
        'hello': 'world again'
    })

@app.route('/')
def hello_world():
    return 'The CLTK API'


def get_cltk_text_dir(lang, corpus='perseus'):
    """Take relative filepath, return absolute"""
    cltk_home = os.path.expanduser('~/cltk_data')
    text_dir = os.path.join(cltk_home, lang.casefold(), 'text', lang.casefold() + '_text_' + corpus, 'json')
    return text_dir


def open_json(fp):
    """Open json file, return json."""
    with open(fp) as fo:
        return json.load(fo)


# Simple example
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# Simple example
class TodoSimple(Resource):
    def get(self, todo_id):
        return {'example with token': todo_id}


# Simple examples
api.add_resource(TodoSimple, '/todo/<string:todo_id>')
# api.add_resource(HelloWorld, '/hello')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
