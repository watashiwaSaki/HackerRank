# Enter your code here. Read input from STDIN. Print output to STDOUT

b, g = map(float, input().split())
n = int(input())
q = b/g
p = 1-q

ans = q * (p**(n-1))
print(round(ans,3))