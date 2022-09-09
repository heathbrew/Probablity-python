"""
From the following list = ["I","am","writing","a","program"], 
Randomly sample 1200 words. For the word “am” collect the right most 
neighbour words, call it as a sample space for the word “am”. Now 
compute the probability of all words in the sample space for the word “am”.

 a) when seed value is 80

 b) when seed value is 50         

 

Note:- Truncate the result upto 3 decimal places and make it without numpy package.
"""
import random
import numpy as np
A = ["I","am","studying","in","BU"]

n = int(input())
random.seed(n)
B = [random.choice(A) for i in range(1200)]
i_list = []
w_list = []
a = []
am_list = []
prog_list = []
for i in range(len(B)):
    if(B[i] == "BU"):
        if(B[i+1] == "I"):
            i_list.append(B[i+1])
        
        elif(B[i+1] == "am"):
            am_list.append(B[i+1])
        
        elif(B[i+1] == "in"):
            a.append(B[i+1])
        
        elif(B[i+1] == "studying"):
            w_list.append(B[i+1])
        
        elif(B[i+1] == "BU"):
            prog_list.append(B[i+1])
        
space = len(i_list) + len(am_list) + len(a) + len(w_list) + len(prog_list)
print('In the sample space for the word "BU":')
p_i = round(len(i_list)/space,3)
p_am = round(len(am_list)/space,3)
p_a = round(len(a)/space,3)
p_w = round(len(w_list)/space,3)
p_prog = round(len(prog_list)/space,3)
print('Probability of "I" is ' + str(p_i))
print('Probability of "am" is ' + str(p_am))
print('Probability of "writing" is '+ str(p_w))
print('Probability of "a" is ' + str(p_a))
print('Probability of "program" is ' + str(p_prog))