#uses python3
import sys
import numpy as np


def max_dot_prod(a,b):
    a.sort()
    b.sort()
    return np.dot(a,b)

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = np.array(data[1:(n+1)])
    b = np.array(data[(n+1):])
    print(max_dot_prod(a,b))
