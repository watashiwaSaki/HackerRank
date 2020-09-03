# Enter your code here. Read input from STDIN. Print output to STDOUT

l1, l2 = map(float, input().split())

a1 = 160 + 40 * (l1+l1**2)
a2 = 128 + 40 * (l2+l2**2)

print(round(a1,3))
print(round(a2,3))