from methods.seed_set_methods import ALGORITHMS, greedy_seed_set, WTSS
from methods.cost_functions import FUNCTIONS, random_cost
from methods.euristics import EURISTICS, f1
from methods.cascade import influence_diffusion
from shared.const import GRAPH_PATH
import networkx as nx
from shared.plotting import plot_graph_seed_set, plot_graph_influenced_nodes, get_graph_positions

def main():
    graph    = nx.read_gml(GRAPH_PATH)
    BUDGET   = 100
    plot     = True

    seed_set = WTSS(graph, BUDGET, random_cost, f1)
    influenced_nodes = influence_diffusion(graph, seed_set)

    print(f"Seed set: {len(seed_set)}")
    print(f"Influenced nodes: {len(influenced_nodes)}")
    
    if plot:
        pos = get_graph_positions(graph)
        plot_graph_seed_set(graph, seed_set, pos)
        plot_graph_influenced_nodes(graph, influenced_nodes, pos)

if __name__ == "__main__":
    main()


