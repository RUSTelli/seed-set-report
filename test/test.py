from methods.seed_set import ALGORITHMS
from methods.cost_functions import FUNCTIONS
from methods.cascade import influence_diffusion
from shared.const import GRAPH_PATH
import networkx as nx
from shared.plotting import plot_algorithm_trend

def main():
    # Set up the graph and parameters.
    graph    = nx.read_gml(GRAPH_PATH)
    BUDGET   = 50
    plot     = True
    SIMUL_NO = 20

    for alg_name, algorithm in ALGORITHMS:
        for function_name, cost_function in FUNCTIONS:
            result = generate_series(algorithm, cost_function, BUDGET, simulations=SIMUL_NO)
            # Plot the results.
            if plot:
                x = [budget for budget, _, _ in result]
                y = [influenced_nodes for _, _, influenced_nodes in result]
                plot_algorithm_trend(x, y, f"{alg_name}_{function_name}")


def generate_series(algorithm, cost_function, budget, simulations=10):
    """
    Generate a series of seed sets for a given algorithm, cost function, and heuristic.
    """
    # Set up.
    graph = nx.read_gml(GRAPH_PATH)
    BUDGET = 100
    budgets = [BUDGET/10*i for i in range(1, 11)]
    result= []

    for budget in budgets:
        avg_seed_set = 0
        avg_influenced_nodes = 0
        for i in range(simulations):
            # Run the algorithm
            seed_set = algorithm(graph, budget, cost_function)
            influenced_nodes = influence_diffusion(graph, seed_set)
            avg_seed_set += len(seed_set)
            avg_influenced_nodes += len(influenced_nodes)
        avg_seed_set //= simulations
        avg_influenced_nodes //= simulations
        result.append((budget, avg_seed_set, avg_influenced_nodes))    
    return result

if __name__ == "__main__":
    main()


