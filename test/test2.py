from methods.seed_set import ALGORITHMS
from methods.cost_functions import FUNCTIONS
from methods.euristics import EURISTICS

from shared.const import GRAPH_PATH
from methods.cascade import influence_diffusion
import networkx as nx
from shared.plotting import plot_graph_seed_set, plot_graph_influenced_nodes, get_graph_positions

def main():
    # Set up.
    graph = nx.read_gml(GRAPH_PATH)
    GRAPH_CAMERA = get_graph_positions(graph)
    BUDGET = 100
    plot = True
    # also fix random seed?


    for algorithm in ALGORITHMS:
        for cost_function in FUNCTIONS:
            for euristic in EURISTICS:
                seed_set = algorithm(graph, BUDGET, cost_function, euristic)
                influenced_nodes = influence_diffusion(graph, seed_set)

                if plot:
                    plot_graph_seed_set(graph, seed_set, GRAPH_CAMERA)
                    plot_graph_influenced_nodes(graph, influenced_nodes, GRAPH_CAMERA)

if __name__ == "__main__":
    main()