## Smallest Missing Number: Python interview with a FAANG Engineer

# Give an array of unique non-negative integers, find the smallest non negative
# integer not present in the given list

## Example: input: array = [0,1,2,4]
## Output: 3



"""
Way 1: Sort the list with a python inline library: .sort() (TimeComplexity: O(nlog(n))

Sort--> Loop over the list and the first one not found while comparing 
the current to next where next = current+1 is the missing number.
Thats it.


Total Complexity: O(nlog(n)) + the looping part worst: n --> Total worst case
then is:  O(nlog(n))
"""

from typing import List, Any

def get_smallest_int(num_list:list)->int:
	num_list.sort() #sort already replaces the num_list with new num_list sorted one with same variable nambe

	if len(num_list)==0: 
		#Case empty list given:
		#not valid
		raise Exception("empty list")
	else:
		#normal list

		for idx in range(len(num_list)-1):
			current_num = num_list[idx]
			next_num = num_list[idx+1]

			if not next_num==current_num+1:
				return current_num+1 #smallest non -negative integer.


"""
Way 2: Can we do better? yes lets say we dont use the inbuilt sorting function 
from python: So in theory its impossible to go less than n. So n is the minium
worst or in best case 2 indices. O(1)

Lets think we use 2 pointers. one from left and one from right.

Since we want to have sorted as well as find the smalles one 
we can do both simultaneously.
"""

def swap(left,right):
	temp = None
	temp = left
	left = right 
	right = temp
	return left,right


def get_smallest_int_2pointers(num_list:list):
	#Track smalles and largest.
	if len(num_list)%2:
		even = True
		left_mid = len(num_list)//2-1
	
	else:
		odd = True
		left_mid = len(num_list)//2

	# Now, loop over the number
	# left_pointer increases to the right until middle
	# right_pointer decreases to the left until middle


	for idx in range(left_mid):
		left_pointer=idx
		right_pointer=len(num_list)-1-idx

		print ("idx",idx)
		print ("left_pointer",left_pointer)
		print ("right_pointer",right_pointer)

		left = num_list[left_pointer]
		right = num_list[right_pointer]

		#Compare the left and right side of the equation.
		if not num_list[left_pointer]<=num_list[right_pointer]: #then its ok. left <=right
			
			#Swap left right
			left,right = swap(left,right)

		#No need to modify left and right pointer. since it will
		#move with idx
		# Example idx=0,left=0,right=len(num_list)=3
		# idx=1, left=1,right=2
	return num_list




if __name__ == "__main__":
	num_list = [0,1,4,2]
	#num_list  = [0,1,2,4,5]
	print (get_smallest_int(num_list))
	print (get_smallest_int_2pointers(num_list))


##  Second Question: Find the number of unique shapes inside a grid of matrix

## 
"""
Input: 
# 0 0 0 1
# 1 1 0 1
# 0 1 0 0
# 1 0 0 1
# 1 0 0 1

In python the code will be :list of lists as input. 
Find the ones after looping with double loops.

Then recursively search the neighbourhood: left(-1,0)
right (1,0), up(0,1),down(0,-1) recursively check --> now
how do I count shapes? in another main function everytime
the recursive function breaks: count+=1, keep track of the indices
and append shapes[] each time we will append all the coordinates as list

unique shapes --> set of list check for uniqueness.
"""

#Recursive dfs function, we will have 4 combinations of things here
def dfs(matrix,row,column,current_shape):
	up=column+1
	down=column-1
	left=row+1
	right=row-1
	if matrix[row][up]==1:
		current_shape.append((row,up))
		dfs(matrix,row,up,current_shape)
	elif matrix[row][down]==1:
		current_shape.append((row,down))
		dfs(matrix,row,down,current_shape)
	elif matrix[left][column]==1:
		current_shape.append((left,column))
	 	dfs(matrix,left,column,current_shape)
	 elif matrix[right][column]==1:
	 	current_shape.append((right,column))
	 	dfs(matrix,right,column,current_shape)
	 else:
	 	return current_shape


def count_shapes(input:List[List]):
	shapes = []
	current_shape = []
	shapes.append(current_shape)
	#At the begining we initialise the viisted with zeros where all is false.
	visited = [[0 for column in input[0]] for row in input]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if len(matrix)==0:
				if len(matrix[0])==0:
					return 0 # Case when the matrix given is empty
			# else start here.
			if matrix[i][j]==1:
				current_shape=dfs(matrix,i,j,shapes)
				if current_shape not in shape:
					shape.append(current_shape)
	return len(shape) #length of shape gives the number of unique current shape there.

if __name__ == "__main__":
	input = [[0,0,0,1],[1,1,0,1],[0,1,0,0],[1,0,0,1],[1,0,0,1]]
	count_shapes(input)







