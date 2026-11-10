from graph import create_graph, add_edge, add_directed_edge

#directed = False is in charge of saying if it is directed or not, the base is false, but it can be modified and be if or else
def loader_graph(path, directed=False):
    """Read CSV file (source, target, weight) and return a graph
    if directed is True, edges are stored in one direction only."""

    graph = create_graph()
    with open(path) as file:
        next(file) # skips the header line
        for line in file:
            source, target, weight = line.strip().split(",")
            if directed:
                add_directed_edge(graph, int(source), int(target), int(weight))
            else:
                add_edge(graph, int(source), int(target), int(weight))
    return graph