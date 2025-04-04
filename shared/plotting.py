import networkx as nx
import matplotlib.pyplot as plt
from shared.const import PLOT_PATH
import os

def get_graph_positions(graph: nx.Graph):
    """Calculate and return the positions for the graph nodes"""
    return nx.spring_layout(graph)

# Plot the graph with the seed set
def plot_graph_seed_set(graph: nx.Graph, seed_set: set, pos: dict, config = ""):
    plt.figure(figsize=(10, 8))
    
    # Draw all nodes and edges
    nx.draw_networkx_edges(graph, pos, alpha=0.5)
    nx.draw_networkx_nodes(graph, pos, node_color='lightblue', node_size=300, label='Nodes')
    
    # Highlight the seed set
    nx.draw_networkx_nodes(graph, pos, nodelist=seed_set, node_color='red', node_size=500, label='Seed Set')
    
    # Draw labels
    nx.draw_networkx_labels(graph, pos, font_size=10, font_color='black')
    
    plt.legend(scatterpoints=1)
    plt.title(f"Graph with Seed Set Highlighted (Seed Set Size: {len(seed_set)})")
    plt.axis('off')
    path = os.path.join(PLOT_PATH, f"{config}_seed_set.png")
    plt.savefig(path)
    plt.close()  # Close the figure to free memory

# Plot the graph with the influenced nodes
def plot_graph_influenced_nodes(graph: nx.Graph, influenced_nodes: set, pos: dict, config = ""):
    plt.figure(figsize=(10, 8))
    
    # Draw all nodes and edges
    nx.draw_networkx_edges(graph, pos, alpha=0.5)
    nx.draw_networkx_nodes(graph, pos, node_color='lightblue', node_size=300, label='Nodes')
    
    # Highlight the influenced nodes
    nx.draw_networkx_nodes(graph, pos, nodelist=influenced_nodes, node_color='green', node_size=500, label='Influenced Nodes')
    
    # Draw labels
    nx.draw_networkx_labels(graph, pos, font_size=10, font_color='black')
    
    plt.legend(scatterpoints=1)
    plt.title(f"Graph with Influenced Nodes Highlighted (Influenced Size: {len(influenced_nodes)})")
    plt.axis('off')
    path = os.path.join(PLOT_PATH, f"{config}_influenced_set.png")
    plt.savefig(path)
    plt.close()  # Close the figure to free memory