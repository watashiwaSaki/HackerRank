# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import factorial as fact

def comb(n,r):
    return fact(n)/ (fact(r)* fact(n-r))

b, g = map(float, input().split())
p = b/100
output2 = 0
output1 = 0
n = g

for k in range(0,3):
    output1 = output1 +  p**k * ((1-p)**(n-k)) * comb(n,k) 

for k in range(2,11):
    output2 = output2 +  p**k * ((1-p)**(n-k)) * comb(n,k)

print(round(output1,3))
print(round(output2,3))