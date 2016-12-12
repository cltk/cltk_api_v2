""" hello.py """

import json
import os
import sys

from flask import Flask, jsonify
from flask import request  # for getting query string
# eg: request.args.get('user') will get '?user=some-value'
from flask_restful import Api
from flask_restful import Resource

from werkzeug.exceptions import NotFound

app = Flask(__name__)
api = Api(app)

@app.route('/hello')
def hello():
    return jsonify({
        'hello': 'world again'
    })


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
        return {'This is an example with token': todo_id}

# Simple examples
api.add_resource(TodoSimple, '/todo/<string:todo_id>')
# api.add_resource(HelloWorld, '/hello')


# class CapitainsText(Resource):
#     def get(self):
#         fp_rel = '~/cltk_data/corpora/capitains_text_corpora/greekLit'
#         fp = os.path.expanduser(fp_rel)
#         files = os.listdir(fp)
#         json_files = [file for file in files if file.endswith('.json')]
#         for json_file in json_files:
#             json_file_fp = os.path.join(fp, json_file)
#             with open(json_file_fp) as file_open:
#                 x = json.load(file_open)
#                 return {'x': x}
#         return {'files': json_files}
#
# # http://localhost:5000/lang
# api.add_resource(CapitainsText, '/text_example')


# class CapitainsText(Resource):
#     def get(self):
#         fp_rel = '~/cltk_data/corpora/capitains_text_corpora/greekLit'
#         fp = os.path.expanduser(fp_rel)
#         files = os.listdir(fp)
#         json_files = [file for file in files if file.endswith('.json')]
#         for json_file in json_files:
#             json_file_fp = os.path.join(fp, json_file)
#             with open(json_file_fp) as file_open:
#                 x = json.load(file_open)
#                 return {'x': x}
#         return {'files': json_files}
#
# # http://localhost:5000/lang
# api.add_resource(CapitainsText, '/text_example')


# Available functionality, NLP or text serving
# @app.route('/')
# def hello_world():
#     return {'funcionality': ['nlp', 'text']}


@app.route('/')
def available_functionality():
    return jsonify({'cltk_api_functionality': ['nlp', 'text']})


@app.route('/nlp')
def nlp_functionality():
    return jsonify({'nlp_functionality': 'not yet implemented'})


# attempt at self-describing API; could be done better
@app.route('/text')
def text_functionality():
    return jsonify({'next_level': 'lang'})


# Available langs for texts
class AvailableLangs(Resource):
    def get(self):
        print('avail langs OK')
        return {'available_languages': ['greek', 'latin']}

api.add_resource(AvailableLangs, '/text/lang')


class AvailableText(Resource):
    def get(self, lang):
        repo_rel = '~/cltk_data/corpora/capitains_text_corpora/'
        repo = os.path.expanduser(repo_rel)
        print(repo)
        raise AssertionError
        if lang == 'greek':
            lang_dir = 'greekLit'
        elif lang == 'latin':
            lang_dir = 'latinLit'
        else:
            print('bad lang')
            return NotFound
        lang_dir = os.path.join(repo, lang_dir)
        lang_files = os.listdir(lang_dir)
        lang_files_json = [file for file in lang_files if file.endswith('.json')]

        translation = request.args.get('translation')
        if not translation:
            file_ending = '__grc.json'
        elif translation == 'english':
            file_ending = '__eng.json'
        else:
            print("can't find files")
            return NotFound

        lang_files_filtered = [file for file in lang_files_json if file.endswith(file_ending)]
        lang_files_filtered_rm_end = [name.rstrip(file_ending) for name in lang_files_filtered]

        sys.stdout('everything ok')
        return {'language': lang_files_filtered_rm_end}

api.add_resource(AvailableText, '/text/lang/<string:lang>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
