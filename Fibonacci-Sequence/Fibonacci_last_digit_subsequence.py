#uses python3
import sys
import numpy as np


def last_dig(n1,n2):
    m=10;
    F = np.zeros(m*m+2)
    F[1]=1
    for i in range(2,m*m+2):
        F[i] = (F[i-1] + F[i-2]) % m
        if (F[i] == 1) & (F[i-1]==0):
            period = i-1
    sumn2=(F[(n2+2)%period]-1)%10
    sumn1=(F[(n1+1)%period]-1)%10
    return int((sumn2-sumn1)%10)
    


inp = input().split()
n1, n2 = map(int, inp)
print(last_dig(n1,n2))
