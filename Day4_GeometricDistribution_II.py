# Enter your code here. Read input from STDIN. Print output to STDOUT


b, g = map(float, input().split())
n = int(input())
p = b/g
q = 1-p
ans = 0
for k in range(1,6):
    ans = ans +(p * (q**(k-1)))
print(round(ans,3))
