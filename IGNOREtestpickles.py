import cPickle as pickle

pickle_file = open("pickled_names/african.pkl", 'rb')
pickled = pickle.load(pickle_file)

print pickled