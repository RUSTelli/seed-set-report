from methods.seed_set_methods import ALGORITHMS
from methods.cost_functions import FUNCTIONS
from methods.euristics import EURISTICS

from shared.const import GRAPH_PATH
from methods.cascade import influence_diffusion
import networkx as nx
from shared.plotting import plot_graph_seed_set, plot_graph_influenced_nodes, get_graph_positions

graph = nx.read_gml(GRAPH_PATH)
BUDGET = 100
plot = True


for algorithm in ALGORITHMS:
    for cost_function in FUNCTIONS:
        for euristic in EURISTICS:
            seed_set = algorithm(graph, BUDGET, cost_function, euristic)
            influenced_nodes = influence_diffusion(graph, seed_set)

            if plot:
                pos = get_graph_positions(graph)
                plot_graph_seed_set(graph, seed_set, pos)
                plot_graph_influenced_nodes(graph, influenced_nodes, pos)