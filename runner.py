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
	make_classifier()##

if __name__ == "__main__":
	main()