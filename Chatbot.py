from Classifier import *
from Parser import *

class Chatbot:
	def __init__(self):
		self.classifier = Classifier()
		self.parser = Parser()

	def ask(self, sentence):
		data = self.classifier.classify(sentence)
		sql = self.parser.parse(data)
		print(sql)

if __name__ == '__main__':
	cb = Chatbot()
	cb.ask("感冒了吃什么药比较好")