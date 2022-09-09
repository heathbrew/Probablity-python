"""
In a list mol = ["I","am","writing","a", "PYTHON", "program"], 
Randomly sample 1500 words and print the frequency of each word in 
dictionary form as: {"I": frequency, "am":frequency ,"writing":frequency, 
"a":frequency, "PYTHON":frequency, "program":frequency} when
(1) seed is 25
(2) seed is 50.
"""
import numpy as np
import random
mol = ["I","am","writing","a", "PYTHON", "program"]
a = int(input())

random.seed(a)
c=[]
b= [random.choice(mol) for i in range(1499)]

for i in mol:
    c.append(b.count(i))

d = dict(zip(mol,c))
print(d)