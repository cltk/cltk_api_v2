from flask_restful import Resource, reqparse
from cltk.corpus.arabic.utils.pyarabic import araby 


parser = reqparse.RequestParser()
parser.add_argument('text', type=str, help='Arabic text to strip Harakat from arabic word except Shadda')

class StripHarakat(Resource):
	"""
	POST /nlp/corpus/arabic/utils/pyarabic/araby
	Lemmatizes text string input and returns text with strip Harakat from arabic word except Shadda. 

	Example usage:
	curl -d 'text=الْعَرَبِيّةُ ' localhost/nlp/corpus/arabic/utils/pyarabic/araby
	>>> العربيّة

	"""

	def post(self):
		args = parser.parse_args()
		return araby.strip_harakat(args['text'])

