size = int(input())
x = list(map(int, input().split()))
freq = list(map(int, input().split()))
def new(size, x, freq):
    nlist = []
    for i in range(size):
        nlist = nlist + [x[i]]*int(freq[i])
    return nlist
x = new(size, x, freq)

def median(x):
    if len(x)%2 ==0:
        mid = (len(x)//2)-1
        m = (x[mid] + x[mid+1])/2
    else:
        mid = ((len(x)+1)//2)-1
        m = x[mid]
    return m


if len(x)%2 ==0:
    x = sorted(x)
    Q21 = int(len(x)/2)-1
    Q22 = int(len(x)/2)
    L = x[0:Q22]
    U = x[Q22:]
    value = median(sorted(U))-median(sorted(L))
    print(round(float(value),1))
    
else:
    x = sorted(x)
    Q2 = int((len(x)+1)/2)-1
    L = x[0:Q2]
    U = x[Q2+1:]
    value = median(sorted(U))-median(sorted(L))
    print(round(float(value),1))
