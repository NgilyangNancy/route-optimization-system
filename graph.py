# graph.py

class Graph:
    def __init__(self):
        # Dictionary to store adjacency list
        self.nodes = {}

    def add_edge(self, start, end, weight):
        if start not in self.nodes:
            self.nodes[start] = {}
        if end not in self.nodes:
            self.nodes[end] = {}
        # Undirected graph
        self.nodes[start][end] = weight
        self.nodes[end][start] = weight