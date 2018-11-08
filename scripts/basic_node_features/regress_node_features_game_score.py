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


from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

from sklearn.model_selection import train_test_split

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

    # game dictionaries
    ########################################
    simple_game_features_pkl = DATA_DIR + '/simple_features_by_game.pkl'
    simple_game_features_df = load_pkl(fname = simple_game_features_pkl)

    # ['match_id', 'home_shot_rate', 'home_gain_rate', 'home_loss_rate', 'home_pass_rate', 'home_max_pass', 'home_min_pass', 'home_number_players', 'away_shot_rate', 'away_gain_rate', 'away_loss_rate', 'away_pass_rate', 'away_max_pass', 'away_min_pass', 'away_number_players', 'home_team_id', 'away_team_id', 'goal_dif', 'result']
    print list(simple_game_features_df)

    #blacklist_features_A = ['match_id', 'goal_dif', 'result', 'home_team_id', 'away_team_id']
    #blacklist_features_B = ['match_id', 'result', 'home_team_id', 'away_team_id']

    blacklist_features_A = ['match_id', 'goal_dif', 'result', 'away_team_id']
    blacklist_features_B = ['match_id', 'result', 'away_team_id']


    blacklist_features_list = [blacklist_features_A, blacklist_features_B]

    for blacklist_features in blacklist_features_list:
        print '########## NEW REGRESSION ITERATION ##############'
        print ' '
        print 'blacklist: ', blacklist_features

        X_game_features_list = [feat for feat in list(simple_game_features_df) if feat not in blacklist_features]
        X_game_df = simple_game_features_df[X_game_features_list]
        Y_game_df = simple_game_features_df['result']

        print X_game_df.head()
        print ' '
        print Y_game_df.head()
        print ' '

        X_train, X_test, y_train, y_test = train_test_split(X_game_df, Y_game_df, test_size = 0.2, stratify=X_game_df['home_team_id'])

        print 'TRAIN SIZE: '
        print ' '
        print X_train.shape, y_train.shape
        print 'TEST SIZE: '
        print ' '
        print X_test.shape, y_test.shape





