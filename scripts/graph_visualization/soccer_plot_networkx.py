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

from matplotlib.pyplot import cm

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

league = 'epl'

# MATCH GOAL DICT
########################################
match_goal_dict_fname = DATA_DIR + '/' + league + '_match_goal_dict.pkl'
match_goal_dict = load_pkl(fname = match_goal_dict_fname)


# game dictionaries
########################################
simple_game_features_pkl = DATA_DIR + '/simple_features_by_game.pkl'
simple_game_features_df = load_pkl(fname = simple_game_features_pkl)

# EPL MATCHES DICT
########################################
epl_graph_pkl_fname = DATA_DIR + '/EPL_Games.pkl'
epl_graph_dict = load_pkl(fname = epl_graph_pkl_fname)
epl_graph_columns = list(epl_graph_dict)

# PER PLAYER GOAL DICT
########################################
per_player_goal_dict_fname = DATA_DIR + '/PLAYER_INFO_epl.pkl'
per_player_goal_dict = load_pkl(fname = per_player_goal_dict_fname)

match_ids = epl_graph_dict.keys()

example_match = match_ids[0]

single_match_info = epl_graph_dict[example_match]

home_time_weight_graph_adj = single_match_info[5]

away_time_weight_graph_adj = single_match_info[6]

nodes_list = []

node_role_dict = {}

edge_list = []

for k, v in home_time_weight_graph_adj.iteritems():
    
    player_id_0 = k[0]
    player_id_1 = k[1]

    if player_id_0 in per_player_goal_dict.keys():
        player_info = per_player_goal_dict[player_id_0]
        pname_0 = player_info['playerName'].split(',')[0]
        player_position = player_info['playerPosition']
    else:
        pname_0 = player_id_0
        player_position = pname_0

    node_role_dict[pname_0] =  player_position
    nodes_list.append(pname_0)

    if player_id_1 in per_player_goal_dict.keys():
        player_info = per_player_goal_dict[player_id_1]
        pname_1 = player_info['playerName'].split(',')[0]
        player_position = player_info['playerPosition']
    else:
        pname_1 = player_id_1
        player_position = pname_1


    node_role_dict[pname_1] =  player_position
    nodes_list.append(pname_1)

    print (pname_0, pname_1), v

    if v > 0.0:
        edge_list.append((pname_0, pname_1))


unique_nodes = list(set(nodes_list))

print 'unique_nodes: ', unique_nodes
print ' '
print 'node roles: ', node_role_dict
print ' '
print 'unique_edges: ', edge_list

    #>>> per_player_goal_dict[k[0]]
    # {'playerName': 'Cuellar, Carlos', 'playerPosition': 'Defender', 'team_id': 56, 'fail_goals': 0, 'success_goals': 2} 



#G = nx.DiGraph()
#G.add_edges_from(
#    [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
#     ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])
#
#val_map = {'A': 1.0,
#           'D': 0.5714285714285714,
#           'H': 0.0}
#
#values = [val_map.get(node, 0.25) for node in G.nodes()]
#
## Specify the edges you want here
#red_edges = [('A', 'C'), ('E', 'C')]
#edge_colours = ['black' if not edge in red_edges else 'red'
#                for edge in G.edges()]
#black_edges = [edge for edge in G.edges() if edge not in red_edges]
#
## Need to create a layout when doing
## separate calls to draw nodes and edges
#pos = nx.spring_layout(G)
#nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
#                       node_color = values, node_size = 500)
#nx.draw_networkx_labels(G, pos)
#nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
#nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
#plot_fname = 'example_networkx.pdf'
#plt.savefig(plot_fname)
