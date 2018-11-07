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

    league = 'epl'

    # MATCH GOAL DICT
    ########################################
    #match_goal_dict_fname = DATA_DIR + '/' + league + '_match_goal_dict.pkl'
    #match_goal_dict = load_pkl(fname = match_goal_dict_fname)

    ## how this looks:
    ## 442366 {'away_team_goal_list': ['Aguero, Sergio', 'Dzeko, Edin'], 'home_team_name': 'Reading', 'home_team_id': 108, 'away_team_name': 'Manchester City', 'team_id_goal_list': [43, 43], 'away_team_id': 43, 'home_team_goal_list': []}
    ## 442367 {'away_team_goal_list': ['Dempsey, Clint', 'Adebayor, Emmanuel'], 'home_team_name': 'Stoke City', 'home_team_id': 110, 'away_team_name': 'Tottenham Hotspur', 'team_id_goal_list': [110, 6, 6], 'away_team_id': 6, 'home_team_goal_list': ["N'Zonzi, Steven"]}

    ## EPL MATCHES DICT
    #########################################
    #epl_graph_pkl_fname = DATA_DIR + '/EPL_Games.pkl'
    #epl_graph_dict = load_pkl(fname = epl_graph_pkl_fname)

    # game dictionaries
    ########################################
    simple_game_features_pkl = DATA_DIR + '/simple_features_by_game.pkl'
    simple_game_features_dict = load_pkl(fname = simple_game_features_pkl)

    #simple_game_team_features_pkl = DATA_DIR + '/simple_features_by_team_game.pkl'
    #simple_game_team_features_dict = load_pkl(fname = simple_game_team_features_pkl)


