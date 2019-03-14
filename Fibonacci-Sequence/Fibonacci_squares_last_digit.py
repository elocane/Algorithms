#uses python3
import numpy as np 

def last_dig(n):
    F = np.zeros(n+2)
    F[1] = 1
    for i in range(2,n+2):
        F[i] = (F[i-1]+F[i-2]) % 10
    return int((F[n]*F[n+1]) % 10)
    
n = int(input()) % 60
print(last_dig(n))
