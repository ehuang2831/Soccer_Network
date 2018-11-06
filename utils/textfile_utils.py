import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pickle
import random

np.random.seed(42)

"""
sort a dictionary by value
"""

def sort_dict_value(sample_dict = None, reverse_mode = False, sort_index = 1):

    sorted_dict = sorted(sample_dict.items(), key=lambda x: x[sort_index], reverse = reverse_mode)

    return sorted_dict

"""
write a dict to a pkl file for saving
"""

def write_pkl(fname = None, input_dict = None):
    with open(fname, 'wb') as f:
        pickle.dump(input_dict, f)

"""
load the contents of a pkl file

"""

def load_pkl(fname = None):
    with open(fname, 'rb') as f:
        out_dict = pickle.load(f)
    return out_dict

