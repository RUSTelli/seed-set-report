import random
import networkx as nx
import math
import numpy as np


def random_cost(graph: nx.Graph , node) -> int:
    return random.randint(1, 13)

def half_node_degree_cost(graph: nx.Graph, node) -> int:
    return math.ceil(graph.degree(node) / 2)

def kcore_degree_cost(graph: nx.Graph, node) -> int:
    """Original cost combining k-core number and degree diversity"""
    # Calculate k-core numbers
    core_number = nx.core_number(graph)
    
    # Calculate degree diversity (standard deviation of neighbor degrees)
    neighbor_degrees = [graph.degree(n) for n in graph.neighbors(node)]
    diversity = np.std(neighbor_degrees) if neighbor_degrees else 0
    
    # Combine components (core number weighted more heavily)
    return math.ceil(
        0.7 * core_number[node] +  # Emphasize network position
        0.3 * diversity +          # Reward nodes connecting diverse neighbors
        0.1 * graph.degree(node)   # Mild degree penalty
    )

FUNCTIONS = [
    ("random",    random_cost), 
    ("half d(u)", half_node_degree_cost), 
    ("kcore",     kcore_degree_cost),
]