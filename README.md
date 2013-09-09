ethnicityguesser
================

DOCUMENTATION:

Usage:

-- From the Python interpreter:

FROM SCRATCH:

Instantiation:

>>> from runner import make_classifier
>>> mxec = make_classifier()


Training: (note that make_classifier already passes in training tokens)

>>> mxec.train()

Classification: (After training)
>>> mxec.classify('leventhal')
'jewish'
>>> mxec.classify('sekhri')
'indian'

------------------------------------------------------------------------

FROM PICKLE:

Instantiation:

>>> import cPickle as pickle
>>> pickle_file = open('pickled_classifiers/<insert pickle file here, e.g jewishandindian.pkl', 'rb')
>>> mxec = pickle.load(pickle_file)
>>> pickle_file.close()

Training: Done for you

Classification:
>>> mxec.classify('leventhal')
'jewish'
>>> mxec.classify('sekhri')
'indian'

------------------------------------------------------------------------

pickled_classifiers directory is full of pickled ([list of names], 'ethnicity') pairs

pickled_classifiers is full of pickled trained classifiers