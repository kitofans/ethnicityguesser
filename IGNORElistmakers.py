import cPickle as pickle
import os, sys, io
import re


# #### ---- JEW.TXT ---- ####
# import time
# f = open("names_textfiles/jew.txt", 'r')
# names = []
# for line in f:
# 	if len(line) > 1:
# 		match = re.search("\W", line)
# 		if match is None:
# 			names.append(line)
# 		else:
# 			match_index = match.start(0)
# 			names.append(line[:match_index])

# to_pickle = (names, "jewish")

# pickle_file = open("pickled_names/jewish.pkl", 'wb')
# pickle.dump(to_pickle, pickle_file)
# pickle_file.close()


# print names


# WORKS FOR: INDIAN, SPANISH, CHINESE, CZECH, DANISH, FRENCH, JAPANESE
import time
eth = "korean"
f = open("names_textfiles/%s.txt" % eth, 'r')
names = []
for orgline in f:
	orgline = orgline.rstrip('\r')
	orgline = orgline.rstrip('\n')
	orgline = orgline.rstrip('\r')
	line = orgline
	if len(line) > 1:
		match = re.search("\w", line)
		if match is None:
			continue
		else:
			match_index = match.start(0)
			names.append(line[match_index:])

to_pickle = (names, eth)

pickle_file = open("pickled_names/%s.pkl" % eth, 'wb')
pickle.dump(to_pickle, pickle_file)
pickle_file.close()


print to_pickle




# f = open("names_textfiles/african.txt", 'r')
# names = []
# for line in f:
# 	# print line
# 	splits = line.split(' ')
# 	if splits[0].isupper():
# 		if splits[1].isupper():
# 			names.append(splits[0].title() + ' ' + splits[1].title())
# 		else:
# 			names.append(splits[0].title())

# print names
# to_pickle = (names, 'african')
# # sys.exit(1)
# pickle_file = open("pickled_names/african.pkl", 'wb')
# pickle.dump(to_pickle, pickle_file)
# pickle_file.close()