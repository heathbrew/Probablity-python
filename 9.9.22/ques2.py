"""
Ram and Mohan were headed to Domino's to get some pizza. They were debating 
among themselves over who would pay the bill. When their probability teacher 
suddenly approached, she questioned, "Why are you fighting?" Mohan said, “I 
don't want to pay money for pizza”. “Whoever will solve this probability question 
will be exempted to pay or the last one have to pay the pizza cost” the teacher 
asked. The question is,

Assume that X can take on the values given in the file (numbers.txt). 
Calculate the CDF of the random variable X. 

Consider the result for:

1. X=2

2. X=4

3. X=6

4. X=8
"""
with open("Input_Numbers.txt") as f:
    sample_space = f.readlines()
for i in range(len(sample_space)):
    sample_space[i] = int(sample_space[i].strip("\n"));
x = []
for i in sample_space:
    if i not in x:
        x.append(i);
x.sort(reverse=True)
str_value = input()
value = int(str_value[2:])
prob = []

for i in x:
    prob.append(sample_space.count(i)/len(sample_space))
cdf_l = []
prob_l = []
for i in range(len(x)):
    if(x[i]==value):
        for j in range(i,len(x)):
            prob_l.append(prob[j])
            cdf_l.append(x[j])
cdf = 0

for i in range(len(cdf_l)):
    cdf+=prob_l[i]
str_x = "CDF="+str(cdf)
print(str_x)