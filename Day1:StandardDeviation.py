size = int(input())
x = list(map(int, input().split()))

M = sum(x)/size
final = round((sum(map(lambda Xi: (Xi-M)*(Xi-M), x))/size)**0.5,1)
print(final)
