from flask_restful import Resource, reqparse
from cltk.stem.lemma import LemmaReplacer
from cltk.tokenize.word import WordTokenizer


"""
TODO: Download necessary corpora on application start or via Dockerfile? 

from cltk.corpus.utils.importer import CorpusImporter

corpus_importer = CorpusImporter('latin')
corpus_importer.import_corpus('latin_models_cltk')

"""

parser = reqparse.RequestParser()
parser.add_argument('text', type=str, help='Latin text to be lemmatized')

class Lemmatize(Resource):
	"""
	POST /nlp/lemmatize/latin/simple
	Lemmatizes text string input and returns lemmas 

	Example usage:
	curl -d 'text=quid faciat laetas segetes' localhost/nlp/lemmatize/latin/simple
	>>> [
		"quis1",
		"facio",
		"laeto",
		"seges"
	]

	"""

	def post(self):
		lemmatizer = LemmaReplacer('latin')
		word_tokenizer = WordTokenizer('latin')

		args = parser.parse_args()
		tokens = word_tokenizer.tokenize(args['text'])
		lemmatized = lemmatizer.lemmatize(tokens)

		return lemmatized

