size = int(input())
x = list(map(int, input().split()))
#print(round(np.percentile(x, [25, 50, 75])[0],0))
def median(x):
    if len(x)%2 ==0:
        mid = (len(x)//2)-1
        m = (x[mid] + x[mid+1])/2
    else:
        mid = ((len(x)+1)//2)-1
        m = x[mid]
    return m

if size%2 ==0:
    x = sorted(x)
    Q21 = int(size/2)-1
    Q22 = int(size/2)
    L = x[0:Q22]
    U = x[Q22:]
    print(int(median(sorted(L))))
    print(int(median(sorted(x))))
    print(int(median(sorted(U))))
    
else:
    x = sorted(x)
    Q2 = int((size+1)/2)-1
    L = x[0:Q2]
    U = x[Q2+1:]
    print(int(median(sorted(L))))
    print(int(median(sorted(x))))
    print(int(median(sorted(U))))
