from NLTKMaxentEthnicityClassifier import NLTKMaxentEthnicityClassifier as mxec
import sys, io, os
import cPickle as pickle

def unpickle(string):
	pickle_file = open(string, 'rb')
	to_ret = pickle.load(pickle_file)
	return to_ret
	
def make_classifier():
	all_toks = []
	indian_toks = unpickle('pickled_names/indian.pkl')
	jewish_toks = unpickle('pickled_names/jewish.pkl')
	all_toks.append(indian_toks)
	all_toks.append(jewish_toks)
	classifier = mxec(all_toks)
	return classifier

def main():
	all_toks = []
	indian_toks = unpickle('pickled_names/indian.pkl')
	jewish_toks = unpickle('pickled_names/jewish.pkl')
	all_toks.append(indian_toks)
	all_toks.append(jewish_toks)
	classifier = mxec(all_toks)
	classifier.train()

if __name__ == "__main__":
	main()