"""
Longest Path in a Directed Graph:
Python interview with a meta engineer


Given a direct graph, find the length of longest
path from each node.

Ref: Definition of directed graph means every node 
is connected to every other node.
"""


"""
1. I decide to represent my graph as a dictionary


1-->0-->3
2.      4

{1:[0,2],
0:[1,3,2,4],
3: [0,4],
4:[3,0]
}

Longest path from any node to any node. Traverse the graph:
and save path length.
"""

def dfs(graph,node,visited,current_length):
	visited[node] = True #if visited set to true
	max_length=current_length
	for neighbor in graph.get(node,[]):
		if not visited[neighbor]:
			max_length = max(max_length,dfs(graph,neighbor,visited,current_length+1))

	visited[node]=False
	return max_length


def longest_path(graph):
	"""
	graph: Dictionary
	"""
	max_path_length = 0
	#Define visited: set all nodes to False at the beginning of the 
	#node travel

	visited = {node: False for node in graph} #all nodes are unvisited and set to False.

	for node in graph:
		max_path_length = max(max_path_length,dfs(graph,node,visited,0))
	return max_path_length

if __name__ == "__main__":
	graph = {1:[0,2],
		0:[1,3,2,4],
		2: [],
		3: [0,4],
		4:[3,0]
		}

	print (longest_path(graph))



