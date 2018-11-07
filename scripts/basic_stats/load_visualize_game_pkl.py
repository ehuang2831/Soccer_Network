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


def plot_histogram(count_vector = None, num_bins = None, normed = False, xlabel = None, ylabel = None, title = None, plot_fname = None):

    n, bins, patches = plt.hist(count_vector, num_bins, facecolor='green', alpha=0.75, normed = normed)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(plot_fname)
    plt.close()


if __name__ == '__main__':
    print 'ROOT_SOCCER_DIR: ', ROOT_SOCCER_DIR

    league = 'epl'

    # PER PLAYER GOAL DICT
    ########################################
    per_player_goal_dict_fname = 'results/' + league + '_per_player_goal_dict.pkl'
    per_player_goal_dict = load_pkl(fname = per_player_goal_dict_fname)

    num_goals_vec = [v['success_goals'] for k,v in per_player_goal_dict.iteritems()]

    print 'max goals: ', max(num_goals_vec)
    print 'min goals: ', min(num_goals_vec)

    plot_fname = 'results/' + league + 'per_player_goal_hist.pdf'

    plot_histogram(count_vector = num_goals_vec, num_bins = 20, normed = False, xlabel = 'num goals', ylabel = 'Num players', title = 'Goal distro. by player for scorers (at least 1 goal)', plot_fname = plot_fname)

    # MATCH GOAL DICT
    ########################################
    match_goal_dict_fname = 'results/' + league + '_match_goal_dict.pkl'
    match_goal_dict = load_pkl(fname = match_goal_dict_fname)

    # how this looks:
    # 442366 {'away_team_goal_list': ['Aguero, Sergio', 'Dzeko, Edin'], 'home_team_name': 'Reading', 'home_team_id': 108, 'away_team_name': 'Manchester City', 'team_id_goal_list': [43, 43], 'away_team_id': 43, 'home_team_goal_list': []}
    # 442367 {'away_team_goal_list': ['Dempsey, Clint', 'Adebayor, Emmanuel'], 'home_team_name': 'Stoke City', 'home_team_id': 110, 'away_team_name': 'Tottenham Hotspur', 'team_id_goal_list': [110, 6, 6], 'away_team_id': 6, 'home_team_goal_list': ["N'Zonzi, Steven"]}



