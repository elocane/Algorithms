#uses python3

import sys
import numpy as np

def edit_dist(a,b):
    n = len(a)
    m = len(b)
    D = np.zeros((n+1,m+1))
    for i in range(n+1):
        D[i,0] = i
    for i in range(m+1):
        D[0,i] = i
    for j in range(1,m+1):
        for i in range(1,n+1):
            c = 1
            if a[i-1] == b[j-1]:
                c = 0
            D[i,j] = min(D[i-1,j]+1,D[i,j-1]+1,D[i-1,j-1]+c)
    return int(D[n,m])


if __name__ == "__main__":
    print(edit_dist(list(input()), list(input())))
