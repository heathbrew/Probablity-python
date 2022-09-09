import random
from random import *
def coin_trial():
    heads = 0
    for i in range(100):
        if randint(1,100) >= 50:
        # we use 50 because prob of heads is 0.5 
             heads +=1
    return heads
def simulate(n):
    trials = []
    for i in range(n):
        temp = coin_trial()
        print(temp)
        trials.append(temp) 
        #trials.append(coin_trial())
    return(sum(trials)/n)
print(simulate(5))