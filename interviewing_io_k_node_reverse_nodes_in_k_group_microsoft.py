"""
https://www.youtube.com/watch?v=7DpV3xIpaeA

Given the heade of a linkedin list,reverse the nodes 
of the list k at a tie, and return the modified list.


k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes
is not a multiple of k then left-out nodes  in 
the end should remain as it is.

You may alter the values in the list's nodes, only
nodes themselves may be changed.

Example:

Input head = [1,2,3,4,5], k=2
Output: [2,1,3,4,5]


Input Head = [1,2,3,4,5], k=3
Output: [3,2,1,4,5]

Input Head = [1,2,3,4,5], k=4
Output: [4,3,2,1,5]  

"""
from typing import List

def swap(num1,num2):
	temp = num2
	num2 = num1
	num1 = temp
	return num1, num2

def reverse_k_node(numbers:List,k:int):
	"""
	numbers is list: 
	"""
	assert isinstance(k,int)
	assert isinstance(numbers,list)

	assert (k<=len(numbers))
	#By dividing in case its odd, the middle number stays the same.
	for i in range(k//2):
		numbers[i],numbers[k-1-i] = swap(numbers[i],numbers[k-1-i])

		# in python you can also swap directly
		# you could do like: numbers[i],numbers[k-1-i] = numbers[k-1-i],numbers[i]

	return numbers

if __name__ == "__main__":
	numbers = [1,2,3,4,5] 
	k=3
	num1,num2 = swap(1,3)
	print (num1,num2)
	print (reverse_k_node(numbers,k))

## nice one. Good work on using Binary Sorting Technique for this.

	

