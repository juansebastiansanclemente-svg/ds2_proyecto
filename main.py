#import the def that creates the graph
from pickletools import unicodestring1

from graph import create_graph, add_edge, add_directed_edge, to_undirected
from loader import loader_graph
from checking import get_reachable, is_connected, count_components, has_cycles

#This are all the testings i used in main to see if the def works correctly

"""graph_1 = loader_graph("data/ejemplo_1.csv")
graph_2 = loader_graph("data/ejemplo_2.csv")


loader_graph("data/ejemplo_1.csv")
#this is in charge of saving the empty graph into a new variable
graph = create_graph()
add_edge(graph, 1, 2, 4)
add_edge(graph, 1, 3, 2)

#the same as the one above but giving direction to the edge
directed_graph = create_graph()
add_directed_edge(directed_graph, 1, 2, 4)
is_connected(graph_2)
is_connected(graph_1)
is_connected(loader_graph("data/ejemplo_1.csv", directed=True))
is_connected(loader_graph("data/ejemplo_2.csv", directed=True))
has_cycles(loader_graph("data/ejemplo_1.csv"))
has_cycles(loader_graph("data/ejemplo_2.csv"))
has_cycles(loader_graph("data/ejemplo_3.csv"))
has_cycles(loader_graph("data/ejemplo_4.csv"))
has_cycles(loader_graph("data/ejemplo_5.csv"))
has_cycles(loader_graph("data/ejemplo_1.csv", directed=True))
has_cycles(loader_graph("data/ejemplo_2.csv", directed=True))
has_cycles(loader_graph("data/ejemplo_3.csv", directed=True))
has_cycles(loader_graph("data/ejemplo_4.csv", directed=True))
has_cycles(loader_graph("data/ejemplo_5.csv", directed=True))
has_cycles(loader_graph("data/ejemplo_6.csv", directed=True))
#prints the graphs in terminal
print(graph)
print(directed_graph)
print(loader_graph("data/ejemplo_1.csv", directed = True))
print(get_reachable(graph_2, 1))
print(to_undirected(loader_graph("data/ejemplo_1.csv", directed=True)))
print(count_components(loader_graph("data/ejemplo_1.csv")))
print(count_components(loader_graph("data/ejemplo_2.csv")))
print(count_components(loader_graph("data/ejemplo_3.csv")))
print(count_components(loader_graph("data/ejemplo_4.csv")))
print(count_components(loader_graph("data/ejemplo_5.csv")))
"""

#new test for undirected and directed

for number in range(1, 7):
    path = f"data/ejemplo_{number}.csv"
    undirected = loader_graph(path)
    directed = loader_graph(path, directed = True)

    print(f"ejemplo_{number} undirected:")
    is_connected(undirected)
    has_cycles(undirected)

    print(f"ejemplo_{number} directed:")
    is_connected(directed, directed = True)
    has_cycles(directed, directed = True)

