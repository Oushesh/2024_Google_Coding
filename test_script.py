#Sentiment --> 
# INput: sentences
#Score -1 to 1 0 neutral, extremely negative.
#Sentiment Analysis: classification: 

from typing import List, Any


"""
Definition of class label
lower than -1 up to -1: extremely neg
-1 to 0: neutral
> 0 to 1: positive 
"""

def get_class_label(pred_score:float):
	"""
	input: pred_score:float
	Return: string from extremely neg, 0 
	"""
	output_label = ""
	assert (-1<pred_score<1)
	if pred_score==-1:
		output_label ="extremely neg"
	
	elif -1<=pred_score<0:
		output_label ="neutral"
	
	elif 0<=pred<=1:
		output_label = "positive"
	
	else:
		output_label = "None"
	return output_label


"""
Classify words
1. check for specific words from a list of given words --> usually you would 
use things like word2vec, Gloves to build a 
"""

token_dict = {"kill":0,"someone":2,"flowes":3}
knowledgeBase = {"kill":-1,"assassination":-1,"love":+1,"someone":0}

stemming_dictionary = [("kill,killed,killing",("assssinating","assassination","assassin"))]


def get_token_from_word(word,token_dictionary:dict)->int:
	for key,values in token_dictionary.items():
		if word == key:
			return token_dictionary.get(word,"None")


def predict_sentiment(sentence:List[str]):
	token_dict = {"kill":0,"someone":2,"flowes":3}
	knowledgeBase = {"kill":-1,"assassination":-1,"love":+1,"someone":0}
	sentence_length = len(sentence)

	for word in sentence:
		token_from_word = get_token_from_word(word,token_dict)


	#Get Prediction Score from sentence:
	sentence_score = 0
	for word in sentence:
		for key,values in knowledgeBase.items():
			if word == key:
				score=knowledgeBase[word]
				sentence_score+=score


	#Whole sentence score
	#Mean score of the sentence
	mean_sentence_score = sentence_score/sentence_length

	#Definition of Activation Function
	assert isinstance(mean_sentence_score,float)
	class_label = get_class_label(mean_sentence_score)
	assert isinstance(class_label,str)
	return class_label



if __name__ == "__main__":
	sentence  = "Kill Someone"
	sentence = "Dont kill someone"

	sentence_tokens  = sentence.lower().split(" ")

	#predict_sentiment(sentence_tokens)

	print (predict_sentiment(sentence_tokens))
