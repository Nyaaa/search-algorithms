import random
import string
import pprint
import itertools
from search import a_star, dijkstra, dijkstra_queue


class GenerateGraph:
    """
    Generates a random weighted graph
    Inputs:
        size: amount of nodes to generate
    """

    def __init__(self, size: int):
        self.size = size
        self.node_list = []
        for name, i in zip(self.gen_letters(), range(self.size)):
            self.node_list.append(name)

    @staticmethod
    def gen_letters():
        for i in itertools.count(1):
            for p in itertools.product(string.ascii_uppercase, repeat=i):
                yield ''.join(p)

    def gen_node(self, key: str, num: int = 1) -> dict[str, int]:
        """
        Generates a dictionary of random weighted nodes
        Inputs:
            key: exclude this key
            num: amount of nodes to generate
        """
        keys = [key]
        nodes = {}
        while len(nodes) < num:
            key = random.choice(self.node_list)
            if key not in keys:
                node = dict.fromkeys(key, random.randint(1, 100))
                keys.append(key)
                nodes.update(node)
        return nodes

    def gen_graph(self) -> dict[str, dict[str, int]]:
        """
        Adds random nodes to a dictionary, creates connections
        """
        graph = dict.fromkeys(self.node_list)

        for key in graph:
            rnd = random.randint(1, 10)
            graph[key] = self.gen_node(key, rnd)

        for node, links in graph.items():
            for key, value in links.items():
                graph[key][node] = value

        return graph


pp = pprint.PrettyPrinter(width=250)
gr = GenerateGraph(1000)
graph1 = gr.gen_graph()
pp.pprint(graph1)
print('Nodes:', gr.node_list)

node1 = random.choice(gr.node_list)
node2 = random.choice(gr.node_list)
print('Path:', dijkstra_queue.search(graph1, node1, node2))
