from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt


def find_connected_components(graph):
    visited = set()
    components = []

    for vertex in graph:
        if vertex not in visited:
            component = []
            stack = [vertex]

            while stack:
                current_vertex = stack.pop()
                if current_vertex not in visited:
                    visited.add(current_vertex)
                    component.append(current_vertex)
                    stack.extend(graph[current_vertex])

            components.append(component)

    return components


def print_graph(graph):
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")
    print()


def init_network(graph):
    G = nx.Graph()
    for node, neighbors in graph.items():
        G.add_node(node)
        for neighbor in neighbors:
            G.add_node(neighbor)
            G.add_edge(node, neighbor)
    return G


def count_cycles(graph, cycle_num=3):
    G = nx.Graph()
    for node, neighbors in graph.items():
        G.add_node(node)
        for neighbor in neighbors:
            G.add_node(neighbor)
            G.add_edge(node, neighbor)
    result = set()
    for cycle in nx.simple_cycles(G, cycle_num):
        if len(cycle) == cycle_num:
            cycle = sorted(cycle)
            result.add(tuple(cycle))
    return len(result), result


def visualize_graph(graph):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=700,
        node_color="skyblue",
        font_size=20,
        font_weight="bold",
        edge_color="gray",
        width=2,
        edge_cmap=plt.cm.Blues,
    )
    plt.title("Graph Visualization")
    plt.show()
    print()
