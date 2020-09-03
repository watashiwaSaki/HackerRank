# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
from math import e
wt = float(input())
n = float(input())
mu = float(input())
sigma = float(input())
mu = n * mu
sigma = (n**0.5)*sigma
x = 0

def cumdistri(wt, mu, sigma):
    x = (1/2)*(1 + math.erf((wt-mu)/(math.sqrt(2)*sigma)))
    return round(x,4)

print(cumdistri(wt, mu, sigma))