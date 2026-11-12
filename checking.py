from unittest import result

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


def visited_directed(graph, vertex, visited, on_path):
        """Explore from vertex following arrows; return True if a cycle is found"""
        on_path.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor in on_path:
                return True
            if neighbor not in visited:
                if visited_directed(graph, neighbor, visited, on_path):
                    return True
        on_path.remove(vertex)
        visited.add(vertex)
        return False

def has_directed_cycle(graph):
    """Return true if the directed graph has at least one cycle"""
    visited = set()
    on_path = set()
    for start in graph:
        if start not in visited:
            if visited_directed(graph, start, visited, on_path):
                return True
    return False


def has_cycles(graph, directed=False):
    """Return True if the graph has at least one cycle."""
    if directed:
        result = has_directed_cycle(graph)
        print(f"has_cycles: {result}")
        return result

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
    pass  # Owner: eduardo


def is_forest(graph, directed=False):
    """Return True if the graph is a forest."""
    pass  # Owner: eduardo