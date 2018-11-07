from __future__ import division
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import snap
import numpy as np
import sys,os
from scipy.sparse import *
import itertools
import pandas

# configure paths
####################
ROOT_SOCCER_DIR=os.environ['ROOT_SOCCER_DIR']
sys.path.append(ROOT_SOCCER_DIR)

UTILS_DIR = ROOT_SOCCER_DIR + '/utils/'
sys.path.append(UTILS_DIR)

DATA_DIR = ROOT_SOCCER_DIR + '/data/'
EXAMPLE_GRAPH_DIR = DATA_DIR + '/example_graphs/'

GAME_CSV_DIR = DATA_DIR + '/raw_soccer_csv/'

####################

from basic_snap_utils import *
from textfile_utils import *

if __name__ == '__main__':
    print 'ROOT_SOCCER_DIR: ', ROOT_SOCCER_DIR

    league = 'epl'

    per_player_goal_dict_fname = 'results/' + league + '_per_player_goal_dict.pkl'
    
    per_player_goal_dict = load_pkl(fname = per_player_goal_dict_fname)

    for k,v in per_player_goal_dict.iteritems():
        print k, v

