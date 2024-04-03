"""
FAANG Engineer: Number of unique islands
in the position.


Ref: https://www.youtube.com/watch?v=_QQ96M3qrOI

Count number of unique islands in the space.
How to define unique: sum of coordinates or the unique 
combinations of left and right taken by the DFS
define uniqueness. 
"""
from typing import List

def dfs(island_matrix,row,column,visited,count):
	visited[row][column] = 1
	#Lets assume directions left,right,up and down. 4-neighbourhood strategies
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

	#For every row,col as input add the directions
	for dx,dy in directions:
		nx,ny = row + dx, column + dy

		#Check that we dont move over the boundaries of the matrix.
		if 0<= nx <len(island_matrix) and 0 <=ny<len(island_matrix[0]) and island_matrix[nx][ny]==1 and not visited[nx][ny]:
			#Set the visited to 1 and 
			dfs(island_matrix,nx,ny,visited,count)
	

def count_unique_islands(island_matix)->int:
	"""
	island_matrix: List of lists of int
	return: 
	"""
	pass
	assert all(isinstance(route, list) and all(isinstance(element, int) for element in route) for route in island_matrix)

	if not island_matrix:
		return 0
	
	#Track visited. Start counting once we see 1.
	count = 0
	visited = [[0 for element in row] for row in island_matrix]

	for i in range(len(island_matrix)):
		for j in range(len(island_matrix[0])):
			#Check if element is 1
			if island_matrix[i][j]==1 and not visited[i][j]:
				dfs(island_matrix,i,j,visited,count)
				#Update the count here
				count+=1
	return count


if __name__ == "__main__":
	island_matrix = [
	[1,1,0,0,0,0,0],
	[1,0,0,0,1,1,0],
	[1,0,0,0,0,1,0],
	[0,0,1,1,0,0,0],
	[0,0,1,0,0,1,1],
	[0,0,1,0,0,1,0]
	]

	#There are 4 islands.
	#The islands in the top left, bottom 3rd column 
	# are of the same shape. 

	print (count_unique_islands(island_matrix))

