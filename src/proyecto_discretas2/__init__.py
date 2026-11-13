from .graphs import read_graph


def main() -> None:
    graph = read_graph("data/ejemplo_3.csv")
    print("No dirigido:", graph.adjacency)

    directed_graph = read_graph("data/ejemplo_3.csv", directed=True)
    print("Dirigido:", directed_graph.adjacency)