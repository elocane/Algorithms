#uses python3

import sys
import numpy as np

def matches(n,m,k,a,b,c):
    M = np.zeros((n+1,m+1,k+1))
    path = np.zeros((n+1,m+1,k+1))
    for s in range(1,k+1):
        for j in range(1,m+1):
            for i in range(1,n+1):
                if a[i-1] == b[j-1] and a[i-1] == c[s-1]:
                    M[i,j,s] = M[i-1,j-1,s-1] + 1
                else:
                    M[i,j,s] = max(M[i-1,j,s],M[i,j-1,s],M[i,j,s-1])
    return int(M[n,m,k])
    
def matches2(n,m,a,b):
    M = np.zeros((n+1,m+1))
    for j in range(1,m+1):
        for i in range(1,n+1):
            if a[i-1] == b[j-1]:
                M[i,j] = M[i-1,j-1] + 1
            elif M[i-1,j] >= M[i,j-1]:
                M[i,j] = M[i-1,j]
            else:
                M[i,j] = M[i,j-1]
    return int(M[n,m])

def printfun(a,path,i,j):
    global seq
    if i == 0 or j == 0:
         return seq
    if path[i,j] == 0:
        seq.insert(0,a[i-1])
        printfun(a,path,i-1,j-1)
    elif path[i,j] == 1:
        printfun(a,path,i-1,j)
    elif path[i,j] == 2:
        printfun(a,path,i,j-1)
    else:
        printfun(a,path,i-1,j)
        printfun(a,path,i,j-1)
    return seq


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
    
    data = data[m:]
    k = data[0]
    data = data[1:]
    c = data[:k]
    
    #seq = list()
    #path = matches(n,m,a,b)
    #common = printfun(a,path,n,m)
    #print(path)
    #print(common)
    #doubles = []
    #for i in range(1,n+1):
    #    for j in range(1,m+1):
    #        if path[i,j] == 12:
    #            doubles.append([i,j])
    #print(doubles)
    #lengths = list()
    #for element in doubles:
    #print(matches2(len(common),k,common,c))
    print(matches(n,m,k,a,b,c))


