""" 
Four coins are tossed simultaneously. Let X denote the number of times 
the coin comes up with heads. Compute the CDF values for all possible values of X.
"""
ss = ["HHHH","HHHT","HHTH","HHTT","HTHH","HTHT",
      "HTTH","HTTT", "THHH","THHT","THTH","THTT",
      "TTHH","TTHT","TTTH","TTTT"]

x = input()
count = 0

if "0" in x:
    for i in ss:
        b = i.count('T')
        if b == 0:
            count += 1
    a = count/len(ss)
            
elif "2" in x:
    for i in ss:
        b = i.count('T')
        if b <= 2:
            count += 1
    a = count/len(ss)

elif "3" in x:
    for i in ss:
        b = i.count('T')
        if b <= 3:
            count += 1
    a = count/len(ss)

else:
    for i in ss:
        b = i.count('T')
        if b <= 4:
            count += 1
    a = int(count/len(ss))
print(f"CDF={a}")