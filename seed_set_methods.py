import networkx as nx

def __delta_euristic(euristic:callable, dominating_set:set, node, graph) -> int:
    return euristic(dominating_set.union({node}), graph) - euristic(dominating_set, graph)

def __set_cost(graph:nx.Graph, nodes:set, cost_function:callable) -> int:
    return sum([cost_function(graph, node) for node in nodes])

def greedy_seed_set(graph:nx.Graph, budget:int, cost_function:callable, euristic:callable) -> set:
    # seed set, set of nodes that will be selected
    S_p = set()
    S_d = set()

    while(__set_cost(graph, S_d, cost_function) <= budget):
        S_p = S_d.copy()
        max_node = None
        max_value = 0
        for node in graph.nodes():
            if node not in S_d:
                value = (__delta_euristic(euristic, S_d, node, graph)) / cost_function(graph, node)
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