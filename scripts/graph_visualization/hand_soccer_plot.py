import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

G = nx.DiGraph()

edge_list = [(66797.0, 'Loss'), ('Bardsley', 49688.0), ('Vaughan', 'Loss'), (66797.0, 'Graham'), (66797.0, 'Larsson'), ('Larsson', 49688.0), ('Rose', 58771.0), (58771.0, 59125.0), ('Vaughan', 49688.0), (49688.0, 'Rose'), ('Johnson', 'Larsson'), (58771.0, 'Larsson'), ('Rose', 'Shot'), ('McClean', 'Rose'), ('Johnson', 59125.0), ('Bardsley', 'Rose'), (66797.0, 58771.0), ('Cuellar', 66797.0), (49688.0, 66797.0), (59125.0, 'Gain'), ('Rose', 49688.0), (58771.0, "O'Shea"), ("O'Shea", 'Bardsley'), (58771.0, 'Johnson'), (49688.0, 'Gain'), ('Rose', 'Loss'), ('Rose', 'McClean'), ('Rose', 66797.0), ('Larsson', 'Loss'), ('Bardsley', 59125.0), ('Johnson', 'Gain'), ('Larsson', 'Bardsley'), ('Johnson', 'Shot'), (59125.0, 'Vaughan'), ('Larsson', "O'Shea"), ('McClean', 'Loss'), ('Johnson', 'Bardsley'), (49688.0, 59125.0), ('Larsson', 58771.0), ('Bardsley', 66797.0), (66797.0, 49688.0), ("O'Shea", 'Cuellar'), ('Bardsley', 'McClean'), ('Bardsley', 'Shot'), (66797.0, 59125.0), ('Bardsley', 'Graham'), ('Bardsley', 'Larsson'), ('Graham', 49688.0), ('Johnson', 49688.0), (49688.0, 58771.0), ('Rose', "O'Shea"), ('Graham', 'Gain'), (58771.0, 49688.0), (49688.0, "O'Shea"), ("O'Shea", 'Gain'), (58771.0, 'Cuellar'), (66797.0, "O'Shea"), ('Cuellar', 'Loss'), (49688.0, 'Loss'), ('Graham', 'Johnson'), ('Cuellar', 'Johnson'), (49688.0, 'Johnson'), ('Vaughan', 'Gain'), ('Graham', 59125.0), ('Cuellar', 'Bardsley'), ('Graham', 'Larsson'), ("O'Shea", 59125.0), (59125.0, 58771.0), (49688.0, 'Cuellar'), ("O'Shea", 'Larsson'), ("O'Shea", 'Graham'), ('Bardsley', 'Cuellar'), ('Cuellar', 'Gain'), ('McClean', 'Gain'), (58771.0, 66797.0), ("O'Shea", 66797.0), ('Rose', 'Gain'), (58771.0, 'Loss'), ('Johnson', "O'Shea"), ('Rose', 'Cuellar'), ("O'Shea", 58771.0), (59125.0, 'Loss'), ('McClean', "O'Shea"), ('Johnson', 'Vaughan'), ("O'Shea", 'Johnson'), (59125.0, 'Graham'), (66797.0, 'Gain'), (59125.0, 49688.0), ('Bardsley', 'Loss'), (58771.0, 'Graham'), (66797.0, 'Vaughan'), ('Rose', 'Larsson'), (59125.0, 'Bardsley'), ('Johnson', 'Loss'), ("O'Shea", 'Loss'), ('Rose', 59125.0), ('Graham', 58771.0), ('Rose', 'Johnson'), ('Bardsley', 'Johnson'), ('Bardsley', "O'Shea"), ('McClean', 'Bardsley'), ('Bardsley', 'Gain'), ('Larsson', 'Shot'), (58771.0, 'Rose'), ('Larsson', 'Graham'), ('Johnson', 'McClean'), (49688.0, 'Larsson'), (49688.0, 'Graham'), ('Bardsley', 'Goal'), (49688.0, 'Shot'), ('Larsson', 'Rose'), ('Rose', 'Graham'), (49688.0, 'Bardsley'), ("O'Shea", 'McClean'), ('Johnson', 58771.0), ('Vaughan', 'Rose'), ('Rose', 'Vaughan'), ('Graham', 'Loss'), (59125.0, 'Johnson'), ("O'Shea", 49688.0), ("O'Shea", 'Rose'), ('Vaughan', 58771.0), (58771.0, 'Gain'), ('Larsson', 'Johnson'), ('Larsson', 'Gain'), ('Cuellar', 49688.0)]


G.add_edges_from(edge_list)

#val_map = {'Goal': 1.0,
#           'Gain': 0.8,
#           'Gain': 0.2,
#            'Loss': 0.0}
#
#values = [val_map.get(node, 0.4) for node in G.nodes()]


val_map = {'Goal': 'Red',
           'Gain': 'Purple',
           'Shot': 'Yellow',
            'Loss': 'Green'}


values = [val_map.get(node, 'Cyan') for node in G.nodes()]

# Need to create a layout when doing
# separate calls to draw nodes and edges


pos = nx.spring_layout(G, k=0.5, iterations=20)


#pos = nx.spring_layout(G, scale=0.5)
#nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
#                       node_color = values, node_size = 1500)
nx.draw_networkx_nodes(G, pos, node_color = values, node_size = 2500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
#nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
#nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plot_fname = 'soccer_networkx.pdf'
plt.savefig(plot_fname)
