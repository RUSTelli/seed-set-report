import networkx as nx

def __delta_euristic(euristic:callable, dominating_set:set, node) -> int:
    return euristic(dominating_set.union({node})) - euristic(dominating_set)

def __set_cost(nodes:set, cost_function:callable) -> int:
    return sum([cost_function(node) for node in nodes])

def greedy_seed_set(graph, budget:int, cost_function:callable, euristic:callable) -> set:
    # seed set, set of nodes that will be selected
    S_p = set()
    S_d = set()

    while(__set_cost(S_d, cost_function) < budget):
        S_p = S_d.copy
        max_node = None
        max_value = 0
        for node in graph.nodes():
            if node not in S_d:
                value = __delta_euristic(euristic, S_d, node) / cost_function(node)
                if value > max_value:
                    max_value = value
                    max_node = node
        S_d.add(max_node)
    return S_p
    
    

def WTSS(graph, cost_function, budget):
    pass

def alg3(graph, cost_function, budget):
    pass


ALGORITHMS = [
    greedy_seed_set,
    WTSS,
    alg3,
]