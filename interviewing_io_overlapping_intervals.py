#Overlapping intervals: Python interview with a FAANG 
#engineer

#interviewing_io_intervals.py
#Coding Round in Google: 45 min.

## 40 min of technical part 

## 40 min --> technical part
## Overlapping interval.

"""
What if [1,3] [3,5] ? closed loop --> overlap

assume the interval is sorted, meaning 
first number > second number as definition for a
valid list.

"""
from typing import List

def check_overlap(interval1,interval2):
	assert (interval1[0]<interval1[1])
	assert (interval2[0]<interval2[1])

	#now check that interval1 is lower than interval2

	if min(interval1)<min(interval2):
		interval1=interval1
		interval2=interval2
	else:
		#swap is performed here
		temp = interval2
		interval2=interval1
		interval1=temp

	if interval1[1]<=interval2[0]:
		return True
	else:
		return False


"""
Edge Case: what if the order is reversed the code might 
not work? So the best way is to find the min of all. 
and sort it as interval 1 and interval 2 as the second one.
"""

"""
Question 2: Given N real closed intervals, determine 
whether they overlap or not. 


1. Whether they are all overlapping? or some?
 --> all. i.e. every interval must overlap with 
 at least one another interval other than itself.


Idea 1: Perform pairwise comparison of the entities.
O(n2) complexity else sort: O(nlogn) --> then run the first
function check_overlap  


Idea2: use Binary Sort. 2 pointers meaning we 
1 pointer start at left of the array and the second 
on the right.


1. get min(left) and min (right)
2. if min(left) < min(right) --> True (append) --> in the end
3. 

"""

def sort_intervals(intervals):
	#Check Datatype as input
	return sorted(intervals,key=lambda x:x[0])


def swap_intervals(interval1,interval2):
	#Swap is needed
	temp=interval2
	interval2=interval1
	interval1=temp

	return interval1,interval2

def check_n_overlap(intervals)->bool:
	#Check the Datatype as input.
	"""
	input: List[List] of ints. 
	Ouput: True if every interval has one overlap with one another except itself.
	meaning we are looking for Trues -1 for the length of the intervals
	"""
	overlapped = []
	max = float("-inf")
	assert isinstance(intervals, list) and all(isinstance(sublist, list) and all(isinstance(item, int) for item in sublist) for sublist in intervals)
	sorted_intervals = sort_intervals(intervals)

	#Now from the sorted_intervals we get where all the intervals were true it should less
	# than 1 from the number of elements present in the list
	
	#Loop and pass the pairs here
	for i in range(len(intervals)-1):
		interval1 = intervals[i]
		interval2 = intervals[i+1]
		if interval1[1]>max:
			max=interval1[1]
			if interval1[1]>interval2[1]:
				interval1, interval2 =swap_intervals(interval1,interval2)
		
		elif interval2[1]>max:
			max = interval2[1]
			if interval1[1]>interval2[1]:
				interval1, interval2 =swap_intervals(interval1,interval2)

		overlapped.append(check_overlap(interval1,interval2))
	
	print (overlapped)
	if sum(overlapped) == len(intervals)-1:
		return True
	return False


if __name__ == "__main__":
	interval1 = [1,3]
	interval2 = [3,5]
	interval3 = [4,8]

	print (check_overlap(interval1,interval2))

	#intervals: List of lists of ints
	intervals = [interval1,interval2,interval3]

	sorted_intervals = sort_intervals(intervals)

	print (check_n_overlap(intervals))


# I sort of did a bug here: 

