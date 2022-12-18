import matplotlib.pyplot as plt
import networkx as nx
from dataclasses import dataclass


@dataclass
class Edge:
    node1: str
    node2: str
    weight: int

    def __eq__(self, other):
        return (self.node1 == other.node1 or self.node1 == other.node2) and \
               (self.node2 == other.node1 or self.node2 == other.node2)


def draw(graph):
    lst = []

    for node1, links in graph.items():
        for node2, weight in links.items():
            edge = Edge(node1, node2, weight)
            if edge not in lst:
                lst.append(edge)

    g = nx.Graph()

    for i in lst:
        g.add_edge(i.node1, i.node2, weight=i.weight)

    elarge = [(u, v) for (u, v, d) in g.edges(data=True) if d["weight"] > 50]
    esmall = [(u, v) for (u, v, d) in g.edges(data=True) if d["weight"] <= 50]

    pos = nx.spring_layout(g, scale=2)  # positions for all nodes
    nx.draw_networkx_nodes(g, pos, node_size=700)  # nodes
    nx.draw_networkx_edges(g, pos, edgelist=elarge, width=4)  # edges
    nx.draw_networkx_edges(g, pos, edgelist=esmall, width=4, alpha=0.5, edge_color="b", style="dashed")
    nx.draw_networkx_labels(g, pos, font_size=16, font_family="sans-serif")  # node labels

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
