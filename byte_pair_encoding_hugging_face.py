"""
Tokenization: https://www.youtube.com/watch?v=HEikzVL-lZU
Byte pair Encoding Tokenization Algorithm
"""


"""
Input: Corputs, string or different words
as list of strings


Corpus--> hashmap --> get frequency of each word
Each word --> split --> word.split(" ") --> subword level
This the list of splits

Next function to build pair frequencies of pairs

Also Build on the next side list: vocab

Algorithm now:

1. From pairs:List --> get highest frequency pair 
--> merge it --> add it to vocab.

2. Perform merge in splits list as well  as add it into 
merges that happened


3. What is the condition for stopping and merging.

4. Reference: https://towardsdatascience.com/byte-pair-encoding-subword-based-tokenization-algorithm-77828a70bee0

5. The stopping criteria can be either: the count of tokens or number
of iterations. 

how to define the most efficient: criterion for stopping?


For now just define: number of iterations
"""


def get_merge_rule():
	pass



def split(word:str):
	"""
	input: string
	output: split chars each of type string
	"""
	return [char for char in word] 

"""
Merge Rules: 
List representation: ["element1","element2","merged"]
"""

def merge(merge_rule:list,chars:list,vocab:list):
	#Because of the nature of the BPE: we will 
	#only have
	new_char = [] 
	for rule in merge_rule:
		for i in range(len(chars)-1):
			if chars[i] and chars[i+1] in rule:
				#Both characters present in the rule --> merge them
				#check until merge is found

				#Update chars complete.
				new_char.append(rule[2])

				#Append also the rest of the characters.
				new_char.append([rest_char for rest_char in chars[len(chars)-1-i]])

	return new_char


if __name__ == "__main__":
	number_of_iterations=3
	corpus = "hugs"
	merge_rule = [["l","e","le"],
	["le","a","lea"],
	["lea","r","lear"],
	["lear","n","learn"],
	["e","r","er"],
	["h","u","hu"],
	["hu","g","hug"],
	["i","n","in"],
	["in","g","ing"]
	]
	chars=split(corpus)
	print (chars)

	vocab = []
	print(merge(merge_rule,chars,vocab))

































