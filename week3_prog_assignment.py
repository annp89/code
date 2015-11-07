import collections
import random
import copy

# Specify filename to read the input from
filename = 'kargerMinCut.txt'
with open(filename, 'r') as f:
    initial_graph_dict = collections.defaultdict(list)
    for line in f.read().splitlines():
        # Map int onto each item in the list to cast string number to int
        vertices = list(map(int, line.strip().split("\t")))
        initial_graph_dict[vertices[0]] = vertices[1:]


def edgeContraction(graph_dict, nodeA, nodeB):
    # Combine the adjacency list of NodeA with NodeB and remove NodeB
    graph_dict[nodeA] = graph_dict[nodeA] + graph_dict[nodeB]
    graph_dict.pop(nodeB)

    # Switch all vertices that are NodeB to NodeA since NodeB no longer exists
    for key in graph_dict:
        for index in range(len(graph_dict[key])):
            if graph_dict[key][index] == nodeB:
                graph_dict[key][index] = nodeA

    # (b) For NodeA, ensure that we filter out all the references of NodeA to
    # remove self loops.
    graph_dict[nodeA] = list(filter(lambda x: x != nodeA, graph_dict[nodeA]))
            
    return graph_dict


def find_mininum_cut(graph_dict):
    # Base case is 2
    if len(graph_dict) == 2:
        return len(list(graph_dict.values())[0])
    else:
        # Choose any start vertex
        nodeA = random.choice(list(graph_dict.keys()))
        # Choose any adjacent vertex to the selected start vertex
        nodeB = random.choice(graph_dict[nodeA])
        return find_mininum_cut(edgeContraction(graph_dict, nodeA, nodeB))


# Run the algorithm
NO_OF_RUNS = 1000000
i = 0
length = len(initial_graph_dict)
final_min_cut = length**2 - 1

while i < NO_OF_RUNS:
    # Copy the graph so we dont write over the initial graph
    graph_dict = copy.deepcopy(initial_graph_dict)
    new_no_of_min_cut = find_mininum_cut(graph_dict)
    if new_no_of_min_cut < final_min_cut:
        final_min_cut = new_no_of_min_cut
        print(final_min_cut)
    i += 1