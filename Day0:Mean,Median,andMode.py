import numpy as np
from scipy import stats
size = int(raw_input())
STDIN = list(map(int, raw_input().split()))
#STDOUT = [np.mean(STDIN), np.median(STDIN), stats.mode(STDIN)[0][0]]
#stats.mode(arr) for mode
#for p in STDOUT:
#    print (p)
print(np.mean(STDIN))
print(np.median(STDIN))
print(stats.mode(STDIN)[0][0])
