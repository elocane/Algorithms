# Uses python3
import numpy as np

n = int(input())

F = np.zeros(n+2)
F[1] = 1

for i in range(2,n+1,1):
    F[i] = F[i-1]+F[i-2]

print(int(F[n]))
