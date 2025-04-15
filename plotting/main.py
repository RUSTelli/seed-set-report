from methods.seed_set import ALGORITHMS
from methods.cost_functions import FUNCTIONS
from shared.const import GRAPH_PATH
from methods.cascade import influence_diffusion
import networkx as nx
from get_plots import plot_graph_with_highlighted_nodes, get_graph_positions, plot_algorithm_trend
import argparse

def plot_seed_set_diffusion(budget = 100):
    """
    Plots the seed set and influenced nodes for each algorithm and cost function.
    Args:
        budget (int): The budget for the seed set selection.
    """
    graph = nx.read_gml(GRAPH_PATH)
    GRAPH_CAMERA = get_graph_positions(graph)

    for alg_name, algorithm in ALGORITHMS:
        for func_name, cost_function in FUNCTIONS:
            seed_set = algorithm(graph, budget, cost_function)
            influenced_nodes = influence_diffusion(graph, seed_set)

            config = f"{alg_name} - {func_name}"
            plot_graph_with_highlighted_nodes(
                graph, 
                seed_set, 
                GRAPH_CAMERA, 
                set_type="seed_set", 
                config=config
            )
            plot_graph_with_highlighted_nodes(
                graph, 
                influenced_nodes, 
                GRAPH_CAMERA, 
                set_type="influenced_nodes", 
                config=config
            )    


def plot_budget_influenced_size_graph(max_budget=100, simulations=10):
    def _generate_series(algorithm, cost_function, max_budget=100, simulations=10):
        """
        Runs the 'algorithm' a number of 'simulations' time and average the result accordingly.
        Args:
            algorithm (function): The algorithm to use for seed set selection.
            cost_function (function): The cost function to use for budget calculation.
            max_budget (int): The maximum budget for the seed set selection.
            simulations (int): The number of simulations to run for each budget.
        """
        graph   = nx.read_gml(GRAPH_PATH)
        budgets = [max_budget/10*i for i in range(1, 11)]
        result  = []

        for budget in budgets:
            avg_seed_set = 0
            avg_influenced_nodes = 0
            for _ in range(simulations):
                # Run the algorithm
                seed_set = algorithm(graph, budget, cost_function)
                influenced_nodes = influence_diffusion(graph, seed_set)
                avg_seed_set += len(seed_set)
                avg_influenced_nodes += len(influenced_nodes)
            avg_seed_set //= simulations
            avg_influenced_nodes //= simulations
            result.append((budget, avg_seed_set, avg_influenced_nodes))    
        return result

    """
    Plots the budget vs influenced nodes for each algorithm and cost function.
    Args:
        max_budget (int): The maximum budget for the seed set selection.
        simulations (int): The number of simulations to run for each budget.
    """
    for alg_name, algorithm in ALGORITHMS:
        for function_name, cost_function in FUNCTIONS:
            result = _generate_series(algorithm, cost_function, max_budget, simulations)
            x = [budget for budget, _, _ in result]
            y = [influenced_nodes for _, _, influenced_nodes in result]
            plot_algorithm_trend(x, y, f"{alg_name}_{function_name}")


def main(plot_type):
    """
    Main function to generate plots based on the specified plot type.
    Plots are then found in 'plots/'
    Args:
        plot_type (str): The type of plot to generate. Can be "influenced" or "performances".
    """
    if plot_type == "influenced":
        plot_budget_influenced_size_graph()
    elif plot_type == "performances":
        plot_seed_set_diffusion()
    else:
        raise ValueError(f"Invalid plot_type: {plot_type}")  # argparse ensures this never happens

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate plots for cascade analysis.")
    
    parser.add_argument(
        "--plot_type",
        type=str,
        choices=["influenced", "performances"],  # Only allow these two options
        required=True,
        help='Type of plot to generate. Must be "influenced" (for budget-influenced size) or "performances" (for seed set diffusion).'
    )
    
    args = parser.parse_args()
    main(plot_type=args.plot_type)