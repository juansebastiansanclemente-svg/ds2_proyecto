#in loader is in charge of reading CSV, then this def create an empty graph
def create_graph ():
    """Return an empty graph (a dictionary with no vertices yet)."""
    return {}
# edge = arista, source/target = vertice
def add_edge(graph, source, target, weight):
    """Add an undirected edge between source and target with the given weight."""
    if source not in graph:
        graph[source] = {}
    if target not in graph:
        graph[target] = {}
    graph[source][target] = weight
    graph[target][source] = weight

def add_directed_edge(graph, source, target, weight):
    """Add a directed edge from source to target with given weight"""
    if source not in graph:
        graph[source] = {}
    if target not in graph:
        graph[target] = {}
    graph[source][target] = weight

def to_undirected(graph):
    """Return an undirected copy of graph, ignoring edge directions."""
    undirected = create_graph()
    for source in graph:
        if source not in undirected:
            undirected[source] = {}
        for target, weight in graph[source].items():
            add_edge(undirected, source, target, weight)
    return undirected
