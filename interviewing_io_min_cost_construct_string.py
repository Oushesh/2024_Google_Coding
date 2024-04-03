"""
Reference Question: https://interviewing.io/questions/minimum-cost-to-construct-string
Python: Interview with a Google Engineer
Min Cost to construct a string.

Use ABCD to construct a string.

Suppose you can only use character A, B, C and D to form a string of length n. 
You are also given a 2-D integer array of cost[n][4] meaning for each position (0..n - 1), 
the cost to use each character (0..3 means A..D). cost[i][j] means the cost to put character 
j on position i. You cannot have 2 consecutive positions with the same character.

Calculate the smallest cost to make a string of length n.


We can build arrays like AA, BB, CC,

2 characters, cost = [[2,3,4,5],[7,3,4,1]]

AB, AC.


"""


## Question needs to be better defined and explained. No proper communication
## from interviewer.