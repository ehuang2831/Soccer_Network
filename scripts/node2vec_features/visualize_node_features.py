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
import sklearn

from matplotlib.pyplot import cm
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

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



def run_and_plot_TSNE(X_df = None, Y_df = None, label_map = None, plot_fname = None, title_str = None):

    tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=1000)
    tsne_results = tsne.fit_transform(X_df)

    outcomes = list(set(Y_df))

    color=iter(cm.rainbow(np.linspace(0,1,len(outcomes))))

    for i, outcome in enumerate(outcomes):

        subset_indx = (Y_df == outcome)

        vis_x = tsne_results[subset_indx, 0]
        vis_y = tsne_results[subset_indx, 1]
    
        plt.scatter(vis_x, vis_y, c=next(color), label = label_map[outcome])

    plt.legend()
    plt.title(title_str)
    plt.savefig(plot_fname)
    plt.close()


if __name__ == '__main__':

    league = 'epl'

    # game dictionaries
    ########################################
    node2vec_game_features_pkl = DATA_DIR + '/node2vec_by_game.pkl'
    node2vec_game_features_df = load_pkl(fname = node2vec_game_features_pkl)

    # ['match_id', 'home_shot_rate', 'home_gain_rate', 'home_loss_rate', 'home_pass_rate', 'home_max_pass', 'home_min_pass', 'home_number_players', 'away_shot_rate', 'away_gain_rate', 'away_loss_rate', 'away_pass_rate', 'away_max_pass', 'away_min_pass', 'away_number_players', 'home_team_id', 'away_team_id', 'goal_dif', 'result']
    print list(node2vec_game_features_df)

    blacklist_features = ['match_id', 'goal_dif', 'result', 'home_team', 'away_team']

    X_game_features_list = [feat for feat in list(node2vec_game_features_df) if feat not in blacklist_features]
    X_game_df = node2vec_game_features_df[X_game_features_list]
    Y_game_df = node2vec_game_features_df['result']

    X_norm_game_df = sklearn.preprocessing.normalize(X_game_df, axis=1, copy=True, return_norm=False)

    print X_game_df.head()
    print Y_game_df.head()
    print ' '
    print ' '
    label_map = {-1: 'home loss', 0: 'draw', 1: 'home win'} 


    run_and_plot_TSNE(X_df = X_game_df, Y_df = Y_game_df, label_map = label_map, plot_fname = 'node2vec_unnorm_game_tsne.pdf', title_str = 'T-SNE on home and away team embeddings (node2vec)')

    # now normalize and plot
    run_and_plot_TSNE(X_df = X_norm_game_df, Y_df = Y_game_df, label_map = label_map, plot_fname = 'node2vec_NORM_game_tsne.pdf', title_str = 'T-SNE on home and away team embeddings (normalized, node2vec)')


    #########################################
    print '########'
    print 'NOW PROCESS GAME TEAM DF'
    print ' '
    node2vec_game_team_features_pkl = DATA_DIR + '/node2vec_by_team_game.pkl'
    node2vec_game_team_features_df = load_pkl(fname = node2vec_game_team_features_pkl)

    blacklist_features = ['match_id', 'team_id', 'goals', 'result']
    # ['match_id', 'team_id', 'shot_rate', 'gain_rate', 'loss_rate', 'pass_rate', 'max_pass', 'min_pass', 'number_players', 'home', 'goals', 'result']
    print list(node2vec_game_team_features_df)

    X_game_team_features_list = [feat for feat in list(node2vec_game_team_features_df) if feat not in blacklist_features]

    X_game_team_df = node2vec_game_team_features_df[X_game_team_features_list]
    Y_game_team_result_df = node2vec_game_team_features_df['result']
    Y_game_team_teamID_df = node2vec_game_team_features_df['team_id']

    X_norm_game_team_df = sklearn.preprocessing.normalize(X_game_team_df, axis=1, copy=True, return_norm=False)
    
    label_result_map = {-1: 'loss', 0: 'draw', 1: 'win'}
    run_and_plot_TSNE(X_df = X_game_team_df, Y_df = Y_game_team_result_df, label_map = label_result_map, plot_fname = 'node2vec_unnorm_game_team_result_tsne.pdf', title_str = 'T-SNE on team feature vectors (node2vec), colored by game result')

    run_and_plot_TSNE(X_df = X_norm_game_team_df, Y_df = Y_game_team_result_df, label_map = label_result_map, plot_fname = 'node2vec_NORM_game_team_result_tsne.pdf', title_str = 'T-SNE on team feature vectors (normalized, node2vec), colored by game result')

    label_teamId_map = {}

    for team_id in set(node2vec_game_team_features_df['team_id']):
        label_teamId_map[team_id] = 'team ' + str(team_id)

    run_and_plot_TSNE(X_df = X_game_team_df, Y_df = Y_game_team_teamID_df, label_map = label_teamId_map, plot_fname = 'node2vec_unnorm_game_team_teamId_tsne.pdf', title_str = 'T-SNE on team feature vectors (node2vec), colored by team id')

    run_and_plot_TSNE(X_df = X_norm_game_team_df, Y_df = Y_game_team_teamID_df, label_map = label_teamId_map, plot_fname = 'node2vec_NORM_game_team_teamId_tsne.pdf', title_str = 'T-SNE on team feature vectors (normalized, node2vec), colored by team id')

    
     

