"""
    Q1: Generate 1200 random integers between (140,150). 
    Print the frequency in dictionary as {number:frequency} of all 
    numbers i.e. 140 to 150 while selecting the seed as

(1) when seed value is 10
(2) when seed value is 20
(3) when seed value is 30
"""
import numpy as np
a=int(input())
np.random.seed(a)
b=[np.random.randint(140,150) 
   for i in range(1200)]
f={}
for j in set (b):
    f[j]=b.count(j)
print(f)
