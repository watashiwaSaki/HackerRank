# Enter your code here. Read input from STDIN. Print output to STDOUT


import math
sample,mu,sigma,interval, z=float(input()),float(input()), float(input()), float(input()), float(input())
A = 0
B = 0
def CT(sample,mu,sigma,interval,z):
         
    A = mu - (z* (sigma/(sample**0.5)))
    B = mu + (z* (sigma/(sample**0.5)))
    return round(A,2), round(B,2)

print (CT(sample,mu,sigma,interval, z)[0])
print (CT(sample,mu,sigma,interval, z)[1])