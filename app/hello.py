""" hello.py """

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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
