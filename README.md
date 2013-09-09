ethnicityguesser
================

DOCUMENTATION:

Usage:

-- From the Python interpreter:

Instantiation:

>>> from runner import make_classifier
>>> mxec = make_classifier()


Training: (note that make_classifier already passes in training tokens)

>>> mxec.train()

Classification: (After training)
>>> mxec.classify('leventhal')
'jewish'
>>>mxec.classify('sekhri')
'indian'