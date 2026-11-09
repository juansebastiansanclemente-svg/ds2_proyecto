#import the def that creates the graph
from graph import create_graph, add_edge

#this is in chargue of saving the empty graph into a new variable
graph = create_graph()
add_edge(graph, 1, 2, 4)
add_edge(graph, 1, 3, 2)

print(graph)