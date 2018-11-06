import snap
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pickle
import random

np.random.seed(42)
Rnd = snap.TRnd(42)

"""
    basic stats for a SNAP graph G
"""

def print_stats(G = None, print_mode = False):
    node_count = G.GetNodes()
    edge_count = G.GetEdges()

    if print_mode:
        print "G: Nodes %d, Edges %d" % (node_count, edge_count)

    # 1.2 nodes with self edge
    self_edge_count = snap.CntSelfEdges(G)

    if print_mode:
        print "Count of self edges is G is %d" % self_edge_count

    return node_count, edge_count, self_edge_count


"""
given a node_index, get a list of all neighbors with certain filters
    1. of higher node indices - only_higher_indices
    2. neighbor_mode = 'out', 'in', or 'all'
"""

def get_neighbors_specific_node(G = None, node_index = None, neighbor_mode = 'out', only_higher_indices = True, print_mode = False, higher_value = None):

    NI = get_specific_node(G = G, node_index = node_index, print_mode = False)

    out_neighbor_list = []
    for Id in NI.GetOutEdges():
        out_neighbor_list.append(Id)

    in_neighbor_list = []
    for Id in NI.GetInEdges():
        in_neighbor_list.append(Id)

    union_neighbor_list = list(set(out_neighbor_list).union(in_neighbor_list))

    if neighbor_mode == 'out':
        neighbor_list = out_neighbor_list
    elif neighbor_mode == 'in':
        neighbor_list = in_neighbor_list
    else:
        neighbor_list = union_neighbor_list

    if only_higher_indices:
        filter_neighbor_list = [x for x in neighbor_list if x > higher_value]
    else:
        filter_neighbor_list = neighbor_list

    if print_mode:
        print filter_neighbor_list

    return filter_neighbor_list


"""
    get a random edge from a graph
"""

def get_random_edge(config_graph = None, print_mode = False):
    
    a = config_graph.GetRndNId(Rnd)
    spec_node_details = get_specific_node_details(G = config_graph, node_index = a, print_mode = False) 

    a_node = spec_node_details['spec_node']

    # now get all neighbors of a_node and get a specific link
    out_edge_list = []
    for Id in a_node.GetOutEdges():
        if print_mode:
            print ' '
            print "edge (%d %d)" % (a_node.GetId(), Id)
        edge_tuple = (a_node.GetId(), Id)
        out_edge_list.append(edge_tuple)

    if print_mode:
        print 'set out edge list: ', len(set(out_edge_list))
        print ' '

    if len(out_edge_list) > 0:

        # select a random edge
        random_edge = random.choice(out_edge_list)
        if print_mode:
            print 'random edge: ', random_edge

        a = random_edge[0]
        b = random_edge[1]

        if print_mode:
            print ' '
            print 'a: ', a
            print 'b: ', b
    else:
        a = None
        b = None
        out_edge_list = []
        random_edge = None

    return a, b, out_edge_list, random_edge


"""
    get a node iterator for a specific node_index (scalar)
"""

def get_specific_node(G = None, node_index = None, print_mode = True):

    spec_node = G.GetNI(node_index)

    if print_mode:
        print 'Node ID: ', spec_node.GetId()
        print 'degree: ', spec_node.GetDeg()
        print 'out degree: ', spec_node.GetOutDeg()
        print 'in degree: ', spec_node.GetInDeg()

    return spec_node

"""
    get in degree, out degree, and other details for a node_index of interest
"""

def get_specific_node_details(G = None, node_index = None, print_mode = True):

    spec_node = G.GetNI(node_index)

    spec_node_details = {}
    spec_node_details['spec_node'] = spec_node
    spec_node_details['node_id'] = spec_node.GetId()
    spec_node_details['degree'] = spec_node.GetDeg()
    spec_node_details['out_degree'] = spec_node.GetOutDeg()
    spec_node_details['in_degree'] = spec_node.GetInDeg()

    if print_mode:
        for k, v in spec_node_details.iteritems():
            print k, v

    return spec_node_details

"""
    print all edges in a graph
"""

def traverse_edges(Graph = None):
    for edge in Graph.Edges():
        print edge.GetSrcNId(), edge.GetDstNId()


def getDataPointsToPlot_subset(Graph = None, subset_list = None):
    """
    :param - Graph: snap.PUNGraph object representing an undirected graph

    return values:
    X: list of degrees
    Y: list of frequencies: Y[i] = fraction of nodes with degree X[i]
    """
    ############################################################################
    out_degree_list = [n.GetOutDeg() for n in Graph.Nodes() if n.GetId() in subset_list]

    filter_zero_out_degree_list = [x for x in out_degree_list if x > 0]

    min_out_degree = min(filter_zero_out_degree_list)
    print('min out degree: ', min_out_degree)

    max_out_degree = max(filter_zero_out_degree_list) 
    print('max out degree: ', max_out_degree)

    bins_list = np.arange(min_out_degree,max_out_degree+1)

    hist, bin_edges = np.histogram(filter_zero_out_degree_list, bins = bins_list, density = True)

    X = bins_list[0:-1]
    Y = hist 

    print len(X), len(Y)
    print X[0:5], Y[0:5]

    ############################################################################
    return X, Y

