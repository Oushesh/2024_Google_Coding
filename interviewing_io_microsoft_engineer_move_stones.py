#Reference to Question is: https://www.youtube.com/watch?v=J85mQBBdMCI

"""
Question: Interview with Microsoft Engineer: Move 
Stones over Grid with given grid 3*3. 

[
[1,1,0],
[1,1,1],
[1,2,1]
]

In 1 move, you can move a single stone from its current cell to any other cell
if the 2 cells share a side: meaning they are next to each other.


Return the minimum number of moves required to place 1 stone in each cell.
"""


"""

Assert stones is always positive integer or zero
1. Double loop over the matrix 2D Dimensions of the matrix
2. as long as the value is 1 its ok --> look for zero. (start)
3. Run DFS over there with 4 Directions as neighbourhood: dfs(matrix,row,col,carryon,path)

if value==1: leave untouched. --> move 
loop over all the dimensions if > 1 (Carry on: value-1) --> +1 (end point)

--> retrace the path to 0.
"""


def dfs(matrix,x,y,steps):
	"""
	Definition of directions:
	left: (-1,0)
	right: (1,0)
	up: (0,-1)
	down: (0,1)
	"""
	directions = [(-1,0),(1,0),(0,-1),(0,1)]

	#For every direction: 
	for dx,dy in directions:
		nx,ny = x+dx,y+dy #whether you need it now or later.

		#We check whether the 
		if 0<=nx <len(matrix) and 0<=0<len(matrix[0]) and matrix[nx][ny]==0:
			matrix[nx][ny] = 1
			steps +=1
			dfs(matrix,nx,ny,steps)
	return steps


def get_min_steps(matrix):
	# Find cells with values greater than 1 and perform DFS on it.
	steps = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j]>1:
				matrix[i][j] = 1 
				steps=dfs(matrix,i,j,steps) #Start DFS
				steps+=1

	# Check if all cells are filled with '1s'
	for row in matrix:
		if 0 in row:
			return -1

	return steps

if __name__ == "__main__":
	matrix = [
		[1,1,0],
		[1,1,1],
		[1,2,1]
		]

	matrix = [
		[2,2,0],
		[2,1,1],
		[1,2,1]
	]	

	min_steps = get_min_steps(matrix)
	print (min_steps)
	"""
	1,1,0.      
	1,1,1  --> 0-->1-->1-->2
	1,2,1


	"""
	##  Bare minimum is 1: starting point is 0 and the next point is 2. 
	##  Bare minimum is 2: where to start and how




