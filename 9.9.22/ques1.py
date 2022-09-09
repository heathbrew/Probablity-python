"""
Harry applied for the post of data scientist in Microsoft. 
The director of Microsoft said that you will be hired if you calculate 
the probability of each number in the sample space if a dice with 10 faces 
was rolled randomly N times. He also asked him to compute its expected value. 
Consider the result for

1. Seed value: 150 and Input the value of N: 3

2. Seed value: 100 and Input the value of N: 2

3. Seed value: 50 and Input the value of N: 1

 

Note:- Truncate the result upto 2 decimal places and make it without numpy package.
"""
import random
str_n = input()

n = int(str_n[11:])
random.seed(n)
str_x = input()
x = int(str_x[21:])

possible = [1,2,3,4,5,6,7,8,9,10]
sample_space = [random.choice(possible) for i in range(x)]

events = len(sample_space)
prob = []
bruh = ""
for i in possible:
    prob.append(round(sample_space.count(i)/events,2));
    bruh+=str(round(sample_space.count(i)/events,2))+" "
print(bruh.rstrip())

expected_value = 0;

for i in range(len(prob)):
    expected_value+=round(prob[i]*possible[i],2)
f = round(expected_value,2)
print(f)