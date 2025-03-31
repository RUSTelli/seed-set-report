import random
import networkx as nx
import math


def random_cost(graph: nx.Graph , node) -> int:
    return random.randint(1, 100)

def half_node_degree_cost(graph: nx.Graph, node) -> int:
    return math.ceil(graph.degree(node) / 2)

def third_cost_function(graph, node) -> int:
    pass

FUNCTIONS = [
    random_cost, 
    half_node_degree_cost, 
    third_cost_function,
]