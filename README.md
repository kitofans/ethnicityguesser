ethnicityguesser
================

A machine-learning classifier based on nltk's maxent classifier to guess the ethnicity of a last name.


DEPENDENCIES:
nltk

------------------------------------------------------------------------

CURRENT ETHNICITIES:
african
chinese
czech
danish
french
indian
italian
japanese
jewish
spanish

------------------------------------------------------------------------

DOCUMENTATION:

Note that all methods available to NLTK's MaxentClassifier is available to the ethnicity classifier. Look at NLTKMaxentEthnicityClassifier.py
for information, but in general it is the exact same method name (i.e NLTKMaxentEthnicityClassifier.prob_classify()/classify()/explain() etc).
Only train() works a little differently because the implementation allows a list of names rather than a list of featuresets.

Usage:

-- From the Python interpreter:

FROM SCRATCH:

Instantiation:


\>\>\> from runner import make_classifier
\>\>\> mxec = make_classifier()


Training: (note that make_classifier already passes in training tokens)


\>\>\> mxec.train()


Classification: (After training)


\>\>\> mxec.classify('leventhal')
'jewish'
\>\>\> mxec.classify('sekhri')
'indian'


FROM PICKLE:

Instantiation:

\>\>\> import cPickle as pickle
\>\>\> pickle_file = open('pickled_classifiers/[insert pickle file here, e.g jewishandindian.pkl]', 'rb')
\>\>\> mxec = pickle.load(pickle_file)
\>\>\> pickle_file.close()


Training: Done for you

Classification:

\>\>\> mxec.classify('leventhal')
'jewish'
\>\>\> mxec.classify('sekhri')
'indian'


-- In other code (as in a bigger project, etc):

```python
from NLTKMaxentEthnicityClassifier import NLTKMaxentEthnicityClassifier as mxec
classifier = mxec(tokens) ## tokens must be a list of ([list of names], 'ethnicity') pairs. Ethnicities can be repeated.
```

Training and Classification as above.


Pickling:

\>\>\> mxec.pickleme(directory_name)

------------------------------------------------------------------------

pickled_names directory is full of pickled ([list of names], 'ethnicity') pairs

pickled_classifiers is full of pickled trained classifiers