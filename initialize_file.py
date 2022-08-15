#this code just pickles an empty array to a file

import pickle
import sys

#if not len(sys.argv)==2:
#  raise Exception("expected 2 args")
#x=argv[1] # just too afraid that someone will remove entity_type or something
x="Combat/entity_data.txt"

with open(x,"wb") as fil:
  pickle.dump(dict(),fil)