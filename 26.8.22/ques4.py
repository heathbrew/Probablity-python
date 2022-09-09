"""
Q2: Create a function that computes the probability  (up to one decimal place) 
of some number K in a data array

(a) if array is {50,51,51,51,52,53,56,57,57,57} then compute the 
probability of 50, 51, 54, 56, and 57.
"""
a=int(input())
arr=[50,51,51,51,52,53,56,57,57,57]
f=arr.count(a)
print(f/len(arr))