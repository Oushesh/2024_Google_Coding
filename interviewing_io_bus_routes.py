#Ref: https://www.youtube.com/watch?v=dFh4ECKNEZM

"""
Bus Routes: Graph Problem most likely

Example 1:
routes = [[1,2,7],[3,6,7]], source = 1, target = 6

starting point: 1, target: 6
Does starting point exist: the sub-routes?
1->2->7 ---> Find common point in second one: does
a common route exist in seond --> From then only 2 possibilities --> left or right
direction of movement --> add until you read destination.


Edge Cases:
1. If source or target does not exist: route not possible return -1 (False)
2. no common element found between the different subroutes if source and target
   not in same subroute: no route --> return -1 (False)


Space & Time Complexity in the end:


Possibility for further optimisation:
"""

#We will use recurring depth first search to get the route
#directions: left or right.
from typing import List, Any

"""
	Convert the list of routes into a graph representation
	Args: routes(list): List of routes
	Returns: dict: Graph Representation with nodes and keys
"""


def convert_to_graph(routes):
    """
    Convert the list of routes into a graph representation.

    Args:
    routes (list): List of routes.

    Returns:
    dict: Graph representation with nodes as keys and their connections as values.
    """
    
    assert all(instance(route,list) and  all(instance(element,int)  for element in route) for route in routes)

    graph = {}
    for route in routes:
        for i in range(len(route) - 1):
            current_node = route[i]
            next_node = route[i + 1]
            if current_node not in graph:
                graph[current_node] = []
            graph[current_node].append(next_node)

            # Ensure bidirectional connection
            if next_node not in graph:
                graph[next_node] = []
            graph[next_node].append(current_node)

    return graph

"""
DFS: Path: Finding using DFS algorithm
"""

def dfs(graph, start, end, visited=None, path=None):
    """
    Depth-First Search (DFS) to find a path between two nodes in a graph.

    Args:
    graph (dict): Graph representation with nodes as keys and their connections as values.
    start: Starting node.
    end: Ending node.
    visited (set): Set of visited nodes (default: None).
    path (list): Current path being explored (default: None).

    Returns:
    list: Path between the starting and ending nodes, or None if no path exists.
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == end:
        return path

    if start in graph:
        for neighbor in graph[start]:
            if neighbor not in visited:
                new_path = dfs(graph, neighbor, end, visited, path.copy())
                if new_path:
                    return new_path
    return None


if __name__ == "__main__":
    routes = [[1,2,3],[3,6,7],[6,4,9]]

    # Example routes
    #routes = [[1, 2, 7], [3, 6, 7]]
    start = 1
    target = 9

    graph = convert_to_graph(routes)
    print ("graph",graph)

    # Find path from starting to ending point
    path = dfs(graph, start, target)

    print (path)

"""
its like a linked list
Start: 1
Target: 4
Possible Path --> 1,2,3 --> 3,6,7 --> 6,4
Think of directions: left and right as directions 

Google Style interview on and on: get better. Practice and check.
"""






