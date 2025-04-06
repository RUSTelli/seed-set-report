from typing import Callable
import networkx as nx
from networkx.algorithms import community
import math

def greedy_seed_set(
        graph: nx.Graph, 
        budget: int, 
        cost_function:Callable
    ) -> set:
    """
    Greedy algorithm for selecting a seed set of nodes in a graph.
    The algorithm iteratively selects nodes that maximize the increase in the
    euristic function while considering the cost of adding each node to the seed set.
    """

    def delta_euristic(euristic, dominating_set, node) -> int:
        return euristic(dominating_set.union({node}), graph) - euristic(dominating_set, graph)
    def set_cost(nodes: set, cost_function: callable) -> int:
        return sum([cost_function(graph, node) for node in nodes])
    def euristic(dominating_set: set, graph: nx.Graph) -> int:
        return sum(
            min(
                len(set(graph.neighbors(node)).intersection(dominating_set)),
                math.ceil(graph.degree(node) / 2)
            )
            for node in graph.nodes()
        )

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
    

def WTSS(
        graph: nx.Graph, 
        budget:int, 
        cost_function: Callable
    ) -> set:
    """
    WTSS algorithm for selecting a seed set of nodes in a graph.
    The algorithm iteratively selects nodes that maximize the ratio of the cost
    to the degree of the node, while considering the cost of adding each node to the seed set.
    The algorithm stops when the budget is exceeded or when no more nodes can be added.

    """
    
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
                if total_cost + cost[v] <= budget and delta[v] > 0:
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



def CACESS(
    graph: nx.Graph, 
    budget: int, 
    cost_function: Callable, 
    resolution: float = 1.0
) -> set:
    """
    Community-Aware Cost-Effective Seed Selection (CACESS) Algorithm
    
    1. Detect communities using Louvain method
    2. Within each community:
       a. Calculate node efficiency = (degree * betweenness) / cost
       b. Select top candidates until community budget is exhausted
    3. Global optimization pass to refine selection
    
    Args:
        graph: Input graph
        budget: Total activation budget
        cost_function: Function (G, node) -> cost
        resolution: Community detection resolution parameter
        
    Returns:
        Seed set of nodes that maximizes influence across communities
    """
    
    # Phase 1: Community Detection
    communities = community.louvain_communities(graph, resolution=resolution, seed=42)
    
    # Phase 2: Intra-Community Selection
    seed_set = set()
    remaining_budget = budget
    community_budgets = {i: budget//len(communities) for i in range(len(communities))}
    
    for i, comm in enumerate(communities):
        comm_graph = graph.subgraph(comm)
        candidates = []
        
        # Calculate node efficiency metrics
        degrees = nx.degree_centrality(comm_graph)
        betweenness = nx.betweenness_centrality(comm_graph)
        
        for node in comm:
            eff = (degrees[node] * betweenness[node]) / cost_function(graph, node)
            candidates.append((eff, node))
            
        # Select nodes within community budget
        candidates.sort(reverse=True)
        local_budget = community_budgets[i]
        
        for eff, node in candidates:
            cost = cost_function(graph, node)
            if cost <= local_budget and node not in seed_set:
                seed_set.add(node)
                local_budget -= cost
                remaining_budget -= cost
                
    # Phase 3: Global Optimization Pass
    candidates = []
    degrees = nx.degree_centrality(graph)
    betweenness = nx.betweenness_centrality(graph)
    
    for node in graph.nodes():
        if node not in seed_set:
            eff = (degrees[node] * betweenness[node]) / cost_function(graph, node)
            candidates.append((eff, node))
    
    candidates.sort(reverse=True)
    
    for eff, node in candidates:
        cost = cost_function(graph, node)
        if cost <= remaining_budget:
            seed_set.add(node)
            remaining_budget -= cost
            
    return seed_set


ALGORITHMS = [    
    ("greedy",    greedy_seed_set),
    ("wtss",      WTSS),
    ("community", CACESS),
]