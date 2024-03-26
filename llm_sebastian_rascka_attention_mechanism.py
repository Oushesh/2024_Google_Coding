"""
Understanding and Coding the 
Self-Attention Mechanism of Large Language
Models from Scratch
"""

#Embedding an Input Sentence:
sentence = "Life is short,eat dessert first"

token = {s:i for i,s in enumerate(sorted(sentence.replace(',','').split()))}
print (token)



if __name__ == "__main__":
