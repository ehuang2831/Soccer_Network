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
    simple_game_features_df = load_pkl(fname = simple_game_features_pkl)

    # ['match_id', 'home_shot_rate', 'home_gain_rate', 'home_loss_rate', 'home_pass_rate', 'home_max_pass', 'home_min_pass', 'home_number_players', 'away_shot_rate', 'away_gain_rate', 'away_loss_rate', 'away_pass_rate', 'away_max_pass', 'away_min_pass', 'away_number_players', 'home_team_id', 'away_team_id', 'goal_dif', 'result']
    print list(simple_game_features_df)

    blacklist_features = ['match_id', 'goal_dif', 'result', 'home_team_id', 'away_team_id']

    X_game_features_list = [feat for feat in list(simple_game_features_df) if feat not in blacklist_features]
    X_game_df = simple_game_features_df[X_game_features_list]
    Y_game_df = simple_game_features_df['result']


    print X_game_df.head()
    print Y_game_df.head()
    print ' '
    print ' '


    ########################################
    print '########'
    print 'NOW PROCESS GAME TEAM DF'
    print ' '
    simple_game_team_features_pkl = DATA_DIR + '/simple_features_by_team_game.pkl'
    simple_game_team_features_df = load_pkl(fname = simple_game_team_features_pkl)

    blacklist_features = ['match_id', 'team_id', 'goals', 'result']
    # ['match_id', 'team_id', 'shot_rate', 'gain_rate', 'loss_rate', 'pass_rate', 'max_pass', 'min_pass', 'number_players', 'home', 'goals', 'result']
    print list(simple_game_team_features_df)

    X_game_team_features_list = [feat for feat in list(simple_game_team_features_df) if feat not in blacklist_features]

    X_game_team_df = simple_game_team_features_df[X_game_team_features_list]
    Y_game_team_df = simple_game_team_features_df['result']

    print X_game_team_df.head()
    print Y_game_team_df.head()
    print ' '
    print ' '



