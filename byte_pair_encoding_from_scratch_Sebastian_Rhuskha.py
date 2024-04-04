"""
Sebastian Rhuska: implementing Byte pair Encoding for LLM 
from scratch.

Sample Example: 
input_string = "aaabdaabac"

all_english_alphabets="abcdefghijklmnopqrstuvwxyz"

Build a frequency hash map. 
Get all the alphabets not found. 
Choose 1 randomly from not found.

1 combo, 2 combo,
replace it with common letters "aa" 

new string becomes "XabdXabac"

Check again: hash map
From hash map: we check whats not found:

Perform replacment
Y=ab

New String: XYdXYac

XY=aaab
Y=ab

Keep replacing up until all the numbers
are from the unknonws we picked before.
"""


def byte_pair_encoding(input_string:str):
	"""
	input_string:str
	"""
	pass

	alphabets = "abcdefghijklmnopqrstuvwxyz"
	#initialise the  
	alphabets_dict = {char:0 for char in alphabets}
	string_dict = {char:0 for char in input_string}
	while True:

		for char in input_string:
			strong_dict[char]+=1
			alphabets_dict[char]+=1

		#Now we did build a hashmap and the chars with 
		#Recognize the neighbouring ones 
	return None 


if __name__ == "__main__":
	input_string = "aaabdaabac"
	print (byte_pair_encoding(input_string))

