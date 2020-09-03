# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
from math import e
mu, sigma = map(float, input().split())
l1 = float(input())
l2, l3 = map(int, input().split())

x = 0

def cumdistri(l, mu, sigma):
    x = (1/2)*(1 + math.erf((l-mu)/(math.sqrt(2)*sigma)))
    return x

p2 = cumdistri(l3,mu,sigma) - cumdistri(l2,mu,sigma)
print(round(cumdistri(l1,mu,sigma),3))
print(round(p2,3))

