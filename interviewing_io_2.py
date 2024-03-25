#Link to the youtube video of the session needed to build the question
#https://www.youtube.com/watch?v=J1Hr3gFcwfU


"""
Given a pattern such as "il8n" --> for internationalization

il8n --> start, number of strings (in between),end

f6k should match facebook, but not focus

function signature: doesMatch(pattern,input)

"""


"""
Question 2: Given an mxn integers matrix, return the 
length of the longest increasing path in the matrix. 
From each cell you can either move in 4 directions: left,right,up or down.

INput: list[List]
[
[9,9,4],
[6,6,8],
[2,1,1]
] Output: 4

Explanation: The length of the increasing path is [1,2,6,9]
"""


"""
Way 1: DFS(matrix,row,column)
Start from the minimum.

if neighbourhood is  greater than the current  recursively call
the function. at the same time, append the paths.
then at the end: sum(length of the list of the paths) 
"""

#Fixed: messed the rows and columns here.
def dfs(matrix,row,col,visited,min_entry,path):
	# Define the directions for exploring neighbours (up,down,left,right)

	visited[row][col] = True

	# Explore the neighbours
	up = row - 1 
	down = row + 1
	left = col + 1
	col = col - 1

	
	
	if 0<=up <len(matrix) and 0<=col <len(matrix[0]) and not visited[left][col]:
		if matrix[up][col]>min_entry:
			print ("here",matrix[up][col])
			# Update the minimum entry
			min_entry = matrix[up][col]
			visited[uo][col] = True
			path.append(matrix[up][col])
			dfs(matrix,left,col,visited,min_entry,path)
	
	elif 0<=down<len(matrix) and 0<=col and len(matrix[0]) and not visited[down][col]:
		if matrix[down][col]>min_entry:
			# Update the minimum entry
			visited[down][col] = True
			min_entry = matrix[down][col]
			path.append(matrix[down][col])
			dfs(matrix,right,col,visited,min_entry,path)

	elif 0<=row <len(matrix) and 0<= left <len(matrix[0]) and not visited[row][left]:
		if matrix[row][left]>min_entry:
			visited[row][up] = True
			# Update the minimum entry
			min_entry = matrix[row][left]
			path.append(matrix[row][left])
			dfs (matrix,row,up,visited,min_entry,path)

	elif 0<=row <len(matrix) and 0<= left <len(matrix[0]) and not visited[row][right]:
		if matrix[row][right]>min_entry:
			visited[row][right] = True

			# Update the minimum entry
			min_entry = matrix[row][right]
			path.append(matrix[row][right])
			dfs(matrix,row,down,visited,min_entry,path)

	return path


def get_longest_increasing_path(matrix):
	path = []
	if not matrix:
		return 0

	rows, cols = len(matrix),len(matrix[0])
	min_entry = float('inf')
	min_row,min_col = 0,0

	#Iteratively find the minimum entry of the matrix 
	for i in range(rows):
		for j in range(cols):
			if matrix[i][j] < min_entry:
				min_entry = matrix[i][j]

				#Then get the indices for the rows and columns
				min_row,min_col = i,j

	print (min_row)
	print (min_col)
	print ("min_entry",matrix[min_row][min_col])

	#Initialise the visited matrix
	visited = [[False] * cols for _ in range(rows)]


	#Then perform dfs on it 

	discovered_paths=dfs(matrix,min_row,min_col,visited,min_entry,path)
	print (discovered_paths)

	print (len(discovered_paths))

	return discovered_paths

"""
New Code: with simplified stuffs.
"""

def dfs(matrix, row, col, visited, min_entry, path):
    # Define the directions for exploring neighbors (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    visited[row][col] = True
    path.append(matrix[row][col])  # Append the current cell value to the path
    
    max_path = path[:]  # Initialize the maximum path with the current path
    
    # Explore neighbors
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        #print (dr)
        #print (dc)
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and matrix[new_row][new_col] > min_entry and not visited[new_row][new_col]:
            # Recursive call to DFS for each unvisited neighbor with a greater value than min_entry
            new_path = dfs(matrix, new_row, new_col, visited, matrix[new_row][new_col], path[:])  # Pass a copy of the current path
            if len(new_path) > len(max_path):  # Update the maximum path if the new path is longer
                max_path = new_path
    
    return max_path

def get_longest_increasing_path_chatgpt(matrix):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    min_entry = float('inf')
    min_row, min_col = 0, 0

    # Iteratively find the minimum entry of the matrix
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] < min_entry:
                min_entry = matrix[i][j]
                min_row, min_col = i, j

    # Initialize the visited matrix
    visited = [[False] * cols for _ in range(rows)]

    # Then perform DFS on it
    longest_path = dfs(matrix, min_row, min_col, visited, min_entry, [])

    print ("longest_path",longest_path)

    print ("length of longest_path",len(longest_path))
    return longest_path

if __name__ == "__main__":
    matrix = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]

    # Get longest increasing path
    longest_path = get_longest_increasing_path(matrix)
    print("Longest increasing path:", longest_path)


    longest_path = get_longest_increasing_path_chatgpt(matrix)
    print ("longest path by gpt",longest_path)

#Check why the code from my side was flawed. Done the code was flawed because the row and column?
#got interchanged in the code I wrote. 

