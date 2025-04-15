import networkx as nx
import matplotlib.pyplot as plt
from shared.const import PLOT_PATH
import os

def get_graph_positions(graph: nx.Graph):
    """Calculate and return the positions for the graph nodes"""
    return nx.spring_layout(graph)

# Plot the graph with the seed set
def plot_graph_with_highlighted_nodes(graph: nx.Graph, nodes_to_highlight: set, pos: dict, set_type="seed_set", config = ""):
    plt.figure(figsize=(10, 8))
    
    # Draw all nodes and edges
    nx.draw_networkx_edges(graph, pos, alpha=0.5)
    nx.draw_networkx_nodes(graph, pos, node_color='lightblue', node_size=300, label='Nodes')
    
    # Determine color based on set_type
    
    if set_type == 'seed_set':
        highlight_color = 'red'
        config = f"{config} - seed set: {len(nodes_to_highlight)}"
    else:
        highlight_color = 'green'
        config = f"{config} - influenced: {len(nodes_to_highlight)}"
    
    # Highlight the specified nodes
    nx.draw_networkx_nodes(graph, pos, nodelist=nodes_to_highlight, node_color=highlight_color, node_size=500, label=f"{set_type.replace('_', ' ').title()}")
    
    # Draw labels
    nx.draw_networkx_labels(graph, pos, font_size=10, font_color='black')
    
    plt.legend(scatterpoints=1)
    plt.title(f"{config}")
    plt.axis('off')
    path = os.path.join(PLOT_PATH, f"{config}.png")
    plt.savefig(path)
    plt.close()  # Close the figure to free memory

def plot_algorithm_trend(x: list, y: list, config = ""):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title(f"{config}")
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.grid()
    path = os.path.join(PLOT_PATH, f"{config}_algorithm_trend.png")
    plt.savefig(path)
    plt.close()  # Close the figure to free memory