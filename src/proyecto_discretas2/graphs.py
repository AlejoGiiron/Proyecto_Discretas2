class DirectedGraph:
    def __init__(self):
        self.adjacency  = {}                       

    def add_edge(self, source, target, weight):
        if source not in self.adjacency:
            self.adjacency[source] = {}
        self.adjacency[source][target] = weight
        if target not in self.adjacency:
            self.adjacency[target] = {}
        


graph = DirectedGraph()
graph.add_edge("1", "2", 3)
graph.add_edge("2", "3", 1)
graph.add_edge("3", "4", 4)
print(graph.adjacency)


class UndirectedGraph:
    def __init__(self):
        self.adjacency  = {}                       

    def add_edge(self, source, target, weight):
        if source not in self.adjacency:
            self.adjacency[source] = {}
        self.adjacency[source][target] = weight

        if target not in self.adjacency:
            self.adjacency[target] = {}
        self.adjacency[target][source] = weight

        if target not in self.adjacency:
            self.adjacency[target] = {}
        


graph = UndirectedGraph()
graph.add_edge("1", "2", 3)
graph.add_edge("2", "3", 1)
graph.add_edge("3", "4", 4)
print(graph.adjacency)