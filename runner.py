#!/usr/bin/python

from NLTKMaxentEthnicityClassifier import NLTKMaxentEthnicityClassifier as mxec
import sys, io, os
import cPickle as pickle

def unpickle(string):
	pickle_file = open(string, 'rb')
	to_ret = pickle.load(pickle_file)
	return to_ret
	
def make_classifier():
	all_toks = []
	for pickle_file in os.listdir("pickled_names"):
		all_toks.append(unpickle('pickled_names/' + pickle_file))
	classifier = mxec(all_toks)
	return classifier

def main():
	classifier = make_classifier()
	# classifier = unpickle('../ethnicityguesser/pickled_classifiers/danish_irish_chinese_czech_japanese_french_jewish_indian_spanish_italian_.pkl')
	print classifier
	while(True):
		name = raw_input("Enter a name (enter to quit) -->: ")
		if name == "":
			break
		print classifier.classify(name)

if __name__ == "__main__":
	main()
