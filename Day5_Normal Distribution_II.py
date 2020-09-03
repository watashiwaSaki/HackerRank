# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
from math import e
mu, sigma = map(float, input().split())
l1 = float(input())
l2 = float(input())

x = 0

def cumdistri(l, mu, sigma):
    x = (1/2)*(1 + math.erf((l-mu)/(math.sqrt(2)*sigma)))
    return x

print(round(100*(1 - cumdistri(l1,mu,sigma)),2))
print(round(100*(1 - cumdistri(l2,mu,sigma)),2))
print(round(100*cumdistri(l2,mu,sigma),2))