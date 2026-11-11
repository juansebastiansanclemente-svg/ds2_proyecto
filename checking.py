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
    pass  # Owner: sebastian


def is_tree(graph, directed=False):
    """Return True if the graph is a tree."""
    pass  # Owner: eduardo


def is_forest(graph, directed=False):
    """Return True if the graph is a forest."""
    pass  # Owner: eduardo