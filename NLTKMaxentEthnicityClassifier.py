import io, os, sys
from nltk.classify.maxent import MaxentClassifier as mxc

class NLTKMaxentEthnicityClassifier(object):

	def ngrams(self, name, n):
		ngrams = []
		for i in range(len(name) - n + 1):
			ngrams.append(name[i:i+n])
			if len(name[i:i+n]) != n:
				print "PROBLEM PROBLEM PROBLEM!!!!!!!!"

		return ngrams


	def add_prefix_suffix(self,name,n,features):
		features['first_%sgram' % n] = name[:n]
		features['last_%sgram' % n] = name[-n:]



	def featureset(self, orig_name):
		name = orig_name.lower()
		features = {}
		for i in range(1,4):
			if len(name) >= i:
				self.add_prefix_suffix(name, i, features)
		

		for bigram in self.ngrams(name, 2):
			features['has(%s)' % bigram] = True

		for trigram in self.ngrams(name, 3):
			features['has(%s)' % trigram] = True

		features['nameis'] = name
		return features

	def make_toks(self, ethnicity_list):
		toks = []
		names = ethnicity_list[0]
		ethnicity = ethnicity_list[1]


		for name in names:
			toks.append((self.featureset(name),ethnicity))

		return toks


	def train(self):
		self.classifier = mxc.train(self.tokens)

	def classify(self, name):
		features = self.featureset(name)
		output = self.classifier.classify(features)
		return output




#### TRAINING_LISTS MUST BE A LIST OF (LIST_OF_NAMES,STRING_ETHNICITY) PAIRS ###
	def make_train_toks(self, training_lists):
		all_toks = []
		for ethnicity_list in training_lists:
			all_toks += self.make_toks(ethnicity_list)

		return all_toks

	def __init__(self, training_lists):
		self.tokens = self.make_train_toks(training_lists)
