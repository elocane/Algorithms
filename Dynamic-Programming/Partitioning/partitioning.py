#uses python3

import sys
import numpy as np

def partition(n,v):
    if sum(v) % 3 != 0:
        return 0
    if n < 3:
        return 0
    if max(v) > sum(v)/3:
        return 0
    part = sum(v)//3
    matrix = np.zeros((n+1,part+1,part+1))
    matrix[:,0,0] = 1
    for i in range(1,n+1):
        for j in range(0,part+1):
            for k in range(0,part+1):
                if matrix[i-1,j,k] == 1:
                    matrix[i,j,k] = 1 
                elif v[i-1] <= j and matrix[i-1,j-v[i-1],k]:
                    matrix[i,j,k] = 1
                elif v[i-1] <= k and matrix[i-1,j,k-v[i-1]]:
                    matrix[i,j,k] = 1
    return int(matrix[n,part,part])
        

if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int,inp.split()))
    n = data[0]
    v = data[1:]
    print(partition(n,v))
