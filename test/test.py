from methods.seed_set import ALGORITHMS, greedy_seed_set, WTSS
from methods.cost_functions import FUNCTIONS, random_cost
from methods.euristics import EURISTICS, f1
from methods.cascade import influence_diffusion
from shared.const import GRAPH_PATH
import networkx as nx
from shared.plotting import plot_graph_seed_set, plot_graph_influenced_nodes, get_graph_positions

def main():
    # Set up the graph and parameters.
    graph    = nx.read_gml(GRAPH_PATH)
    BUDGET   = 100
    plot     = True
    GRAPH_CAMERA = get_graph_positions(graph)

    seed_set = WTSS(graph, BUDGET, random_cost, f1)
    influenced_nodes = influence_diffusion(graph, seed_set)

    print(f"Seed set: {len(seed_set)}")
    print(f"Influenced nodes: {len(influenced_nodes)}")
    
    if plot:
        plot_graph_seed_set(graph, seed_set, GRAPH_CAMERA)
        plot_graph_influenced_nodes(graph, influenced_nodes, GRAPH_CAMERA)

def generate_series(algorithm, cost_function, euristic, budget):
    """
    Generate a series of seed sets for a given algorithm, cost function, and heuristic.
    """
    # Set up.
    graph = nx.read_gml(GRAPH_PATH)
    BUDGET = 100
    SIMULATIONS = 10
    budgets = [BUDGET/10*i for i in range(1, 11)]
    result= []

    for budget in budgets:
        avg_seed_set = 0
        avg_influenced_nodes = 0
        for i in range(SIMULATIONS):
            # Run the algorithm
            seed_set = algorithm(graph, budget, cost_function, euristic)
            influenced_nodes = influence_diffusion(graph, seed_set)
            avg_seed_set += len(seed_set)
            avg_influenced_nodes += len(influenced_nodes)
        avg_seed_set //= SIMULATIONS
        avg_influenced_nodes //= SIMULATIONS
        result.append((budget, avg_seed_set, avg_influenced_nodes))    
    return result

if __name__ == "__main__":
    main()


