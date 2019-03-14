#uses python3

import sys
import numpy as np

def matches(n,m,a,b):
    M = np.zeros((n+1,m+1))
    for j in range(1,m+1):
        for i in range(1,n+1):
            if a[i-1] == b[j-1]:
                M[i,j] = M[i-1,j-1] + 1
            else:
                M[i,j] = max(M[i-1,j], M[i,j-1])
    #print(M)
    return int(M[n,m])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]
    
    print(matches(n,m,a,b))
