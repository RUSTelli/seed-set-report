from seed_set_methods import ALGORITHMS
from cost_functions import FUNCTIONS
from euristics import EURISTICS

from const import GRAPH_PATH
from cascade import influence_diffusion
import networkx as nx
from plotting import plot_graph_seed_set, plot_graph_influenced_nodes, get_graph_positions

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