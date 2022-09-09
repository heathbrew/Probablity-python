"""
Q2: Create a function that computes the probability (up to one decimal place) 
of some number K in a data array

(b) if array is {a, a, b, c, x, y, z, z, z, z} then compute the 
probability of a, b, y and z.
"""
a=["a", "a", "b", "c", "x", "y", "z", "z", "z", "z"]
def prob(arr,a):
    con=arr.count(a)
    print(con/len(arr))
i=input()
prob(a,i)