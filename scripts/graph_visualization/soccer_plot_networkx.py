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
import networkx as nx

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

# game dictionaries
########################################
simple_game_features_pkl = DATA_DIR + '/simple_features_by_game.pkl'
simple_game_features_df = load_pkl(fname = simple_game_features_pkl)



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
