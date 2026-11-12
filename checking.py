from graph import to_undirected

def get_reachable(graph, start):
    """Return the set of vertices reachable from start (iterative DFS)"""
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                stack.append(neighbor)
    return visited

def count_components(graph):
    """Return the number of connected components of an undirected graph"""
    visited = set()
    components = 0
    for vertex in graph:
        if vertex not in visited:
            visited |= get_reachable(graph, vertex)
            components += 1
    return components

def is_connected(graph, directed=False):
    """Return True if the graph is connected."""
    if directed:
        graph = to_undirected(graph)
    start = list(graph)[0]
    reachable = get_reachable(graph, start)
    result = len(reachable) == len(graph)
    print(f"is_connected: {result}")
    return result


def has_cycles(graph, directed=False):
    """Return True if the graph has at least one cycle."""
    vertex_count = len(graph)
    edge_count = 0
    for neighbors in graph.values():
        edge_count += len(neighbors)
    edge_count = edge_count // 2
    components = count_components(graph)
    result = edge_count > vertex_count - components
    print(f"has_cycles: {result}")
    return result


def is_tree(graph, directed=False):
    """Return True if the graph is a tree."""
    connected = is_connected(graph, directed)
    cycles = has_cycles(graph, directed)
    result = connected and not cycles
    print(f"is_tree: {result}")
    return result


def is_forest(graph, directed=False):
    """Return True if the graph is a forest."""
    cycles = has_cycles(graph, directed)
    result = not cycles
    print(f"is_forest: {result}")
    return result