import io, os, sys
from nltk.classify.maxent import MaxentClassifier as mxc
from sets import Set
import cPickle as pickle

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
		if '.' in orig_name:
			features['has_punct'] = True
		else:
			features['has_punct'] = False

		for i in range(1,5):
			if len(name) >= i:
				self.add_prefix_suffix(name, i, features)
		

		for bigram in self.ngrams(name, 2):
			features['has(%s)' % bigram] = True

		for trigram in self.ngrams(name, 3):
			features['has(%s)' % trigram] = True

		features['nameis'] = name
		return features



	def make_list(self, item):
		if type(item) is list:
			return item
		else:
			return list(item)

	def make_toks(self, ethnicity_list):
		toks = []
		names = self.make_list(ethnicity_list[0])
		ethnicity = ethnicity_list[1]


		for name in names:
			toks.append((self.featureset(name),ethnicity))

		return toks


	def labels(self):
		return self.classifier.labels()

	def set_weights(self, new_weights):
		self.classifier.set_weights(new_weights)


	def weights(self):
		return self.classifier.weights()

	def train(self):
		tokens = self.make_train_toks(self.training_lists)
		self.classifier = mxc.train(tokens,algorithm="iis")


	def explain(self, name, columns=4):
		features = self.featureset(name)
		self.classifier.explain(features, columns)


	def show_most_informative_features(self, n=10, show='all'):
		self.classifier.show_most_informative_features(n, show)

	def prob_classify(self, name):
		features = self.featureset(name)
		output = self.classifier.prob_classify(features)
		return output

	def classify(self, name):
		features = self.featureset(name)
		output = self.classifier.classify(features)
		return output

	def ethnicities(self):
		return self.ethnicities

	def pickleme(self, pickle_directory):
		ethnicity_string = ''
		for ethnicity in self.ethnicities:
			ethnicity_string += ethnicity + '_'
		pickle_file = open(pickle_directory + '/' + ethnicity_string, 'wb')
		pickle.dump(self, pickle_file)
		pickle_file.close()


	def split_list_crossvalidation(self, list_ethnicity_to_split):
		list_to_split = list_ethnicity_to_split[0]
		ethnicity = list_ethnicity_to_split[1]
		from random import shuffle
		shuffle(list_to_split)
		cutoff_index = int(.9*len(list_to_split))
		train = list_to_split[:cutoff_index]
		holdout = list_to_split[cutoff_index:]
		return (train,ethnicity), (holdout,ethnicity)


	def evaluate_success(self, held_lists):
		total = 0
		correct = 0
		wrong = Set()
		for eth_list in held_lists:
			for name in eth_list[0]:
				total += 1
				label = self.classify(name)
				if label == eth_list[1]:
					correct += 1
				else:
					wrong.add((name, label, eth_list[1]))

		print "CORRECT: %d OF %d." % (correct, total)
		print "WRONGS:"
		print wrong

	def cross_validate(self):
		all_train_list = []
		all_held_list = []
		for ethnicity_list in self.training_lists:
			train_list, held_list = self.split_list_crossvalidation(ethnicity_list)
			all_train_list.append(train_list)
			all_held_list.append(held_list)

		toks = self.make_train_toks(all_train_list)
		self.classifier = mxc.train(toks)
		self.evaluate_success(all_held_list)

#### TRAINING_LISTS MUST BE A LIST OF (LIST_OF_NAMES,STRING_ETHNICITY) PAIRS ###
	def make_train_toks(self, training_lists):
		self.ethnicities = Set()
		all_toks = []
		for ethnicity_list in training_lists:
			all_toks += self.make_toks(ethnicity_list)
			self.ethnicities.add(ethnicity_list[1])
		return all_toks

	def __init__(self, training_lists):
		self.training_lists = training_lists
		# self.tokens = self.make_train_toks(training_lists)
