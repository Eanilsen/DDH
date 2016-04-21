import sys
import subprocess
try:
    import cPickle as pickle
except:
    import pickle



def save_to_file(save_file, in_file):
    out_file = open(save_file, 'wb')
    pickle.dump(in_file, out_file)
    out_file.close()

def load_from_file(save_file):
    in_file = open(save_file, 'rb')
    loaded_save = pickle.load(in_file)
    in_file.close()
    return loaded_save
