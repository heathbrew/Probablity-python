"""
   Four coins are tossed simultaneously. Let X denote the number of times the 
   coin comes up with tail. 
   Compute the PMF values for all possible values of X. 
"""
import numpy as np

s = ["HHHH", "HHHT", "HHTH", "HHTT", "HTHH", "HTHT",
     "HTTH", "HTTT", "THHH", "THHT", "THTH", "THTT", 
     "TTHH", "TTHT", "TTTH", "TTTT"]

x = input();
x = x[-1]
x = int(x)
actual = 0;
for i in s:
    count = 0
    for j in i:
        if(j == 'T'):
            count = count +1
        
    if(count == x):
        actual = actual +1
    
print("PMF=" +str(actual/16))