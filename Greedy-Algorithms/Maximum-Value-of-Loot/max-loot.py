#uses python3
import sys
import numpy as np
from operator import itemgetter


def val(n,W,items):
    val = 0
    weight = 0 
    for i in range(n):
        val += min(items[n-1-i,1],W-weight)*items[n-1-i,0]
        weight += min(items[n-1-i,1],W)
        if weight >= W:
            return val
    return np.dot(items[:,0],items[:,1])

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, W = data[0:2]
    values = np.array(data[2:(2 * n + 2):2])
    weights = np.array(data[3:(2 * n + 2):2])
    dens = values/weights
    items = np.column_stack((dens,weights))
    items = items[np.argsort(items[:,0])]
    opt_value = val(n,W,items)
    print("{:.10f}".format(opt_value))
