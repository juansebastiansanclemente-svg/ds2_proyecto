#import the def that creates the graph
from graph import create_graph, add_edge, add_directed_edge

#this is in charge of saving the empty graph into a new variable
graph = create_graph()
add_edge(graph, 1, 2, 4)
add_edge(graph, 1, 3, 2)

#the same as the one above but giving direction to the edge
directed_graph = create_graph()
add_directed_edge(directed_graph, 1, 2, 4)

#prints the graphs in terminal
print(graph)
print(directed_graph)
