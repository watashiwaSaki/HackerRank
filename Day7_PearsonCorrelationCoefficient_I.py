# Enter your code here. Read input from STDIN. Print output to STDOUT

size = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

Mx = sum(x)/size
My = sum(y)/size

SDx = round((sum(map(lambda Xi: (Xi-Mx)*(Xi-Mx), x))/size)**0.5,1)
SDy = round((sum(map(lambda Yi: (Yi-My)*(Yi-My), y))/size)**0.5,1)

def Pearson(Mx, My, SDx, SDy, x, y):
    Num = sum((x[i] - Mx)* (y[i] - My) for i in range(size))
    Den = size * SDx * SDy
    return round(Num/Den, 3)

print(Pearson(Mx, My, SDx, SDy, x, y))