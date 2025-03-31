import networkx as nx
from algorithms import ALGORITHMS


def __diffusion_condition(influeced_nodes:set, graph:nx.Graph, neighbor):
    neighbors = set(graph.neighbors(neighbor))
    neighbors_influenced = len(influeced_nodes.intersection(neighbors))
    return neighbors_influenced > (graph.degree(neighbor) / 2)

def influence_diffusion(graph:nx.Graph, seed_set: set) -> set:
    influenced_nodes = seed_set.copy()
    while True:
        new_influenced_nodes = set(influenced_nodes)
        for node in influenced_nodes:
            for neighbor in graph.neighbors(node):
                if neighbor not in influenced_nodes:
                    if __diffusion_condition(influenced_nodes, graph, neighbor):
                        new_influenced_nodes.add(neighbor)
        if new_influenced_nodes == influenced_nodes:  # Stop if no new nodes are influenced
            break
        influenced_nodes = new_influenced_nodes
    return influenced_nodes

