from math import factorial as fact

def comb(n,r):
    return fact(n)/ (fact(r)* fact(n-r))

b, g = map(float, input().split())
p = b/(b+g)
output = 0
n = 6
for k in range(3,7):
    output = output +  p**k * ((1-p)**(n-k)) * comb(n,k)

print(round(output,3))