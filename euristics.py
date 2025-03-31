import math
import networkx as nx



def f1(dominating_set: set, graph) -> int:
    sum = 0
    for node in graph.nodes():
        # if the node is not in the dominating set
        neighbors = set(graph.neighbors(node))
        sum += min(
            len(neighbors.intersection(dominating_set)),
            math.ceil(graph.degree(node) / 2)
        )
    return sum


def f2(dominating_set: set, graph) -> int:
    sum = 0
    for node in graph.nodes():
        neighbors = set(graph.neighbors(node))
        for i in range(len(neighbors.intersection(dominating_set))):
            sum += max(
                0,
                math.ceil(graph.degree(node) / 2) - i + 1
            )
    return sum
            

def f3(dominating_set: set, graph) -> int:
    sum = 0
    for node in graph.nodes():
        neighbors = set(graph.neighbors(node))
        for i in range(len(neighbors.intersection(dominating_set))):
            sum += max(
                0,
                (math.ceil(graph.degree(node) / 2) - i + 1)/(node.degree() -i + 1)
            )
    return sum


EURISTICS = [
    f1,
    f2,
    f3
]
