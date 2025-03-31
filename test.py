from algorithms import ALGORITHMS, greedy_seed_set
from cost_functions import FUNCTIONS, random_cost
from euristics import EURISTICS, f1
import networkx as nx

FILE_PATH = "dolphins.gml"


def get_maximal_seedset(graph, cost_function, budget):
    pass


def main():
    graph = nx.read_gml(FILE_PATH)
    seed_set=greedy_seed_set(graph, 1000, random_cost, f1)
    

    #TODO: update graph initialization
    graph = 0
    #TODO: select appropriate budget
    budget = 0

    '''

    for cost_foo in FUNCTIONS:
        for alg in ALGORITHMS:
            pass
        # get seedset
        # get influece
        # plot results''
    '''

if __name__ == "__main__":
    main()


