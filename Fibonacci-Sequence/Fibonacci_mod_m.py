#uses python3
import sys
import numpy as np

#def period(m):
#    F = np.zeros(m*m+2)
#    F[1]=1
#    for i in range(2,m*m+2):
#        F[i] = (F[i-1] + F[i-2]) % m
#        if (F[i] == 1) & (F[i-1]==0):
#            return i-1

def modulo(n,m):
    F = np.zeros(m*m+2)
    F[1]=1
    for i in range(2,m*m+2):
        F[i] = (F[i-1] + F[i-2]) % m
        if (F[i] == 1) & (F[i-1]==0):
            period = i-1
    return int(F[n%period])
    
    
inp = input().split()
n = int(inp[0])
m = int(inp[1])
print(modulo(n,m))
