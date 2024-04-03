"""
Ref: https://www.youtube.com/watch?v=wPkfMuN3DyQ
Min and Max Number of Nodes Between Critical Points:
Python interview with a meta engineer
https://www.youtube.com/watch?v=wPkfMuN3DyQ

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

Its  like in 2 packets.



1. min distance between 2 critical points.
2. max distance between 2 critical points.

if we cant calculate the 2 

Example 1: 
Input: head = [3,1]


Example 2: 
Input: head = [5,3,1,2,5,1,2]
There are 3 criticial points.
Output [1,3]


Lets see: min: 1 (local minima)
max: (local maxima) 5

Critical points are: 1,1,5 
min distance = 6-5 = 1
max distance = 6-3 = 3

Distance is based on the positioning 
of the the local minima and local maxima.

i.e. position minimum: position of 1: 3
position minimum: position of 1: 7
position maximum: position of 5: 6

Compute distances from 3,7,6 (combinations)
min distance: 7-6=1, 6-3=3

needed: function to compute gradient: save local minimum and maximum in a list. (append)
min distance = 1
max distance = 3

"""
from typing import List

def compute_gradient(current:int,future:int)->int:
	assert isinstance(current,int)
	assert isinstance(future,int)

	return future-current

def compute_min_max_distance(critical_points_index:list)->list:
	"""
	input: critical_points_index as list of all the critical points indices
	we compute max value between pairs and min value from them
	example: [1,3,5]
	"""
	#Edge Case as given in the Question
	if len(critical_points_index)<0:

	current_min=min([critical_poins_index[i+1]-critical_poins_index[i]for i in range(len(critical_points_index)-1)])
	current_max=max([critical_poins_index[i+1]-critical_poins_index[i]for i in range(len(critical_points_index)-1)])

	return [current_min,current_max]


def get_dist_critical_points(head:list):
	gradients = [0 for i in head] #also beware to 
	critical_points = []
	critical_points_index = []

	for i in range(len(head)-1):
		current = head[i]
		future = head[i+1]

		current_gradient = compute_gradient(current,future)

		#I append the gradient in case its not None.
		gradients[i]=current_gradient

		#How to iteratively detect local minima and local maxima?
		#Need to detect if we found local minima or local maxima

		#only if both the elements and the previous one are not zeros
		if not gradients[i] ==0 and not gradients[i-1]==0: 
			if gradients[i]>0 and gradients[i-1] <0:
				#we found local minimum
				critical_points_index.append(head[i-1])
				critical_points.append(i-1)

			elif gradients[i]<0 and gradients[i-1]>0:
				#we found local maximum
				critical_points_index.append(head[i-1])
				critical_points.append(i-1)

	#Now that we have critical_points_index and critical_points list
	#compute the min and max distance needed
	return compute_min_max_distance(critical_points_index)

if __name__ == "__main__":
	head = [5,3,1,2,5,1,2]
	print (get_dist_critical_points(head))
	
	#expected output [1,3]


#First Test passed.

"""
Explanation of getting the local minima and maxima:
5,3 --> gradient = -2 --> appended
3,1 --> gradient = -2 --> appended
1,2--> graidnet = +1 --> local minima at 1.
2,5 --> gradient = +3 --> appened
5,1 --> gradient = -4 --> local maxima at 5
1,2 --> gradient = +1 --> local minima at 1
"""

"""
I beat meta engineer awesome.
"""


"""
Question 2: Meta Engineer: Valid Moutain Array-->
Array strictly increasing before that index
and strcitly decreasing aft
"""


