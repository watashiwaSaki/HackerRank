size = int(input())
weight = list(map(int, input().split()))
value = list(map(int, input().split()))
wtsum = sum(map(lambda Xi, Yi: Xi * Yi, weight, value))/sum(value)
x = round(float(wtsum),1)
print(x)
