# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import factorial as fact
from math import e
lamb = float(input())
r = int(input())
prob = 0
prob = ((lamb**r *e**(-lamb))/ fact(r))
print(round(prob,3))