class DirectedGraph:
    def __init__(self):
        self.adjacency  = {}                       

    def add_edge(self, source, target, weight):
        if source not in self.adjacency:
            self.adjacency[source] = {}
        self.adjacency[source][target] = weight
        if target not in self.adjacency:
            self.adjacency[target] = {}

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

def read_graph(path, directed=False):
    if directed:
        graph = DirectedGraph()
    else:
        graph = UndirectedGraph()

    with open(path) as file:
        next(file)
        for line in file:
            parts = line.strip().split(",")
            source, target, weight = parts                
            graph.add_edge(source, target, int(weight))    

    return graph