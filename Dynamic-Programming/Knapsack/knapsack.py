#uses python3

import sys
import numpy as np

def maxgold(W,n,weights):
    maxmatr = np.zeros((n+1,W+1))
    for i in range(1,n+1):
        for j in range(1,W+1):
            maxmatr[i,j] = maxmatr[i-1,j]
            if weights[i-1] <= j:
                maxmatr[i,j] = max(maxmatr[i-1,j],maxmatr[i-1,j-int(weights[i-1])] + weights[i-1])
    return int(maxmatr[n,W])

if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int,inp.split()))
    W = data[0]
    n = data[1]
    weights = data[2:]
    print(maxgold(W,n,weights))

