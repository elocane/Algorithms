#uses python3

import sys
#import random
#import numpy as np

def binary_search(n,a,x):
    maxind = n-1
    minind = 0
    while maxind >= minind:
        midind = (maxind + minind) // 2
        if x == a[midind]:
            return midind
        elif x > a[midind]:
            minind = midind + 1
        else:
            maxind = midind - 1
    return -1

#def linear_search(a,x):
#    for i in range(len(a)):
#        if x == a[i]:
#            return i
#   return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(n, a, x), end = ' ')
    #while True:
    #    n = random.randint(1,100)
    #    a = [0]*n
    #    for i in range(n):
    #        a[i] = random.randint(1,100)
    #    a.sort()
    #    x = random.randint(1,100)
    #    print('a: ',a)
    #    print('x: ',x)
    #    lin = linear_search(a,x)
    #    bin = binary_search(n,a,x)
    #    print('linear: ',lin)
    #    print('binary: ',bin)
    #    if lin == bin:
    #        print('OK')
    #    else:
    #        print('whoops')
    #        break
