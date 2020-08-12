import pandas as pd
import networkx as nx

# Generates a complete network of Emerald ocean with weights (number of lps in between)
def make_network(filename):
    EOdf = pd.read_excel(filename)
    EOGraph = nx.Graph()
    for index in range(len(EOdf)):
        EOGraph.add_edge(EOdf.iloc[index,0], EOdf.iloc[index,1], weight = EOdf.iloc[index,2])
    return EOGraph

# Retuns a list of islands that form the shortest path based on weights as well as total weights
def dijkstra_path(EOGraph, source, target):
    return (nx.dijkstra_path(EOGraph, source, target), nx.dijkstra_path_length(EOGraph, source, target))

if __name__ == '__main__':
    EOGraph = make_network('/home/malcyan/Documents/Logs/Emerald Ocean Network.xlsx')
    print(len(EOGraph.nodes()))
    print(dijkstra_path(EOGraph, 'Admiral Island', 'Aimuari Island'))
