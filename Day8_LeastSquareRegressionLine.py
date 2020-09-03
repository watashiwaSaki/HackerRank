# Enter your code here. Read input from STDIN. Print output to STDOUT

x , y = [], []
for i in range(0,5):
    c, d =map(float,input().split())
    x.append(c)
    y.append(d)
n = 5
sigX = sum(x)
avgX = sigX/n
sigY = sum(y)
avgY = sigY/n

def find_b(n,x,y):
    sqX = sum([i**2 for i in x])
    XY = sum([(x[i]* y[i]) for i in range(n)])
    b = (n*XY - sigX*sigY)/(n*sqX - (sigX**2))
    return b
b = find_b(n,x,y)
a = avgY - (b*avgX)
ans = (b*80 + a)
print(round(ans,3))