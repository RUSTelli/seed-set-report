from typing import Callable
import networkx as nx
import math




def greedy_seed_set(
        graph: nx.Graph, 
        budget: int, 
        cost_function:Callable, 
        euristic: Callable) -> set:
        

    def delta_euristic(euristic, dominating_set, node) -> int:
        return euristic(dominating_set.union({node}), graph) - euristic(dominating_set, graph)
    def set_cost(nodes: set, cost_function: callable) -> int:
        return sum([cost_function(graph, node) for node in nodes])

    # seed set, set of nodes that will be selected
    S_p = set()
    S_d = set()
    while set_cost(S_d, cost_function) <= budget:
        S_p = S_d.copy()
        max_node = None
        max_value = 0
        for node in graph.nodes():
            if node not in S_d:
                value = delta_euristic(euristic, S_d, node)
                value /= cost_function(graph, node)
                if value > max_value:
                    max_value = value
                    max_node = node
        S_d.add(max_node)
    return S_p
    

def WTSS(graph: nx.Graph, budget:int, cost_function: Callable, euristic):
    S = set()
    total_cost = 0
    U = set(graph.nodes())
    cost  = {v: cost_function(graph, v) for v in U}
    delta = {v: graph.degree(v) for v in U}
    k     = {v: math.ceil(graph.degree(v) / 2) for v in U}
    N     = {v: set(graph.neighbors(v)) for v in U}

    while U and total_cost <= budget:
        node = None
        # Case 1: Find node with k[v] = 0.
        for v in U:
            if k[v] == 0:
                node = v
                break

        # Case 2: (delta < k)
        if not node:
            for v in U:
                if delta[v] < k[v]:
                    if total_cost + cost[v] <= budget:
                        node = v
                        S.add(node)
                        total_cost += cost[v]
                    break

        # Case 3: Select node with max (c(v)k(v))/(delta(v)(delta(v)+1))
        if not node:
            max_value = -1
            for v in U:
                if total_cost + cost[v] <= budget:
                    value = (cost[v] * k[v]) / (delta[v] * (delta[v] + 1))
                    if value > max_value:
                        max_value = value
                        node = v

        if not node:
            break  # last statement is 'return S'

        # Update neighbors based on case
        if k[node] == 0:  # Case 1
            for u in N[node]:
                if u in U:
                    k[u] = max(k[u] - 1, 0)
        elif node in S:  # Case 2
            for u in N[node]:
                if u in U:
                    k[u] -= 1

        # Update delta and N for all cases
        for u in N[node]:
            if u in U:
                delta[u] -= 1
                N[u].remove(node)
        U.remove(node)

    return S

def alg3(graph, cost_function, budget):
    pass


ALGORITHMS = [
    greedy_seed_set,
    WTSS,
    alg3,
]