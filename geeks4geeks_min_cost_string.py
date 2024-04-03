"""
https://www.geeksforgeeks.org/minimum-cost-construct-string/

Min Cost to construct a string:

Given a string s (lower cases only), we have
to find the minimum for the given string.


1. Cost 1 unit to add a new string.
2. A sub-string of a new string appended without cost
Input: "geks": 4

start s.

all aphabets in english alphabet.


abab

--> every time add a new alphabet. --> check does ab 
also exist one more time or more times. then cost stays the same.
also build a list of all substrings that exist right

abab is 2
ababs is 3



Approach 1: Naive Approach as described above
Approach 2: Like a dictionary or hashmap

"""
from typing import List

def get_cost(input_string:str)->int:
	pass


def is_substring(full_string,substring)->bool:
	return full_string in substring

def get_cost_hash_map(input_string:str,starting_string:str)->int:
	pass
	"""
	input_string:str
	"""
	assert isinstance(input_string,str)
	assert isinstance(starting_string,str)

	alphabets = "abcdefghijklmnopqrstuvwxyz"

	visited = {char:False for char in alphabets}
	cost = 0
	for i in range(len(input_string)):
		if visited.get(input_string[i],[])==False:
			visited[input_string[i]]=True #since we visited it right now

			cost+=1
	return cost


if __name__ == "__main__":
	input_string = "geks"
	print (get_cost_hash_map(input_string,"s"))


"""
Ref: https://www.geeksforgeeks.org/minimum-cost-construct-string/

"""
