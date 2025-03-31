import networkx as nx
from algorithms import ALGORITHMS

def __diffusion_condition(influeced_nodes:set, graph, neighbor, node):
    return len(influeced_nodes.intersection(set(graph.neighbors(neighbor)))) > node.degree() / 2

def influence_diffusion(graph:nx.Graph, seed_set: set) -> set:
    influenced_nodes = set(seed_set)
    while True:
        new_influenced_nodes = set(influenced_nodes)
        for node in influenced_nodes:
            for neighbor in graph.neighbors(node):
                if neighbor not in influenced_nodes:
                    if __diffusion_condition(influenced_nodes, neighbor, node):
                        new_influenced_nodes.add(neighbor)
        if new_influenced_nodes == influenced_nodes:  # Stop if no new nodes are influenced
            break
        influenced_nodes = new_influenced_nodes
    return influenced_nodes

