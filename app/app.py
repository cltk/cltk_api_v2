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
        return {'Example with token': todo_id}



# Simple examples
api.add_resource(TodoSimple, '/todo/<string:todo_id>')
# api.add_resource(HelloWorld, '/hello')


class TextExample(Resource):
    def get(self):
        # fp = os.path.expanduser('~/cltk_data/json/bede_the_venerable,_saint_673-735__de_locis_santis__unk.json')
        # fp = 'example.json'
        # with open(fp) as file_open:
        #     return json.load(file_open)
        home = os.path.expanduser('~/')
        return {'home_files': os.listdir(home),'home_name': home}  # {"home_name": "/root/", "home_files": [".bashrc", ".profile"]}

# http://localhost:5000/lang
api.add_resource(TextExample, '/text_example')




if __name__ == '__main__':
    app.run(host='0.0.0.0')
