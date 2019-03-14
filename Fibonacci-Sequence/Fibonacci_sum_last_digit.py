#uses python3
import sys
import numpy as np


def last_dig(n):
    m=10;
    F = np.zeros(m*m+2)
    F[1]=1
    for i in range(2,m*m+2):
        F[i] = (F[i-1] + F[i-2]) % m
        if (F[i] == 1) & (F[i-1]==0):
            period = i-1
    return int((F[(n+2)%period]-1)%10)
    
    
n = int(input())
print(last_dig(n))
