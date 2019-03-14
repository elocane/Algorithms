#uses python3

import sys
import random

def lottery(s,p,a,b,x):
    labels = ['l']*s  + ['p']*p + ['r']*s
    points = a + x + b
    allpts = list(zip(points,labels))
    list.sort(allpts, key = lambda x: x[0])
    current = 0
    res = [0]*p
    counter = 0
    for i in range(2*s+p):
        if allpts[i][1] == 'l':
            current += 1 
        if allpts[i][1] == 'r':
            current -= 1 
        if allpts[i][1] == 'p':
            res[counter] = current
            counter += 1
    xorder = [i[0] for i in sorted(enumerate(x), key = lambda x: x[1])]
    temp = list(enumerate(x))
    orig = list(zip(res,xorder))
    list.sort(orig, key = lambda x: x[1])
    result = [0]*p
    for i in range(p):
        print(orig[i][0], end = ' ')
    return
    
def naive(s, p, a, b, x):
    cnt = [0] * p
    for i in range(p):
        for j in range(s):
            if a[j] <= x[i] <= b[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int,inp.split()))
    s = data[0]
    p = data[1]
    a = data[2:2+2*s:2]
    b = data[3:3+2*s:2]
    x = data[2*s+2:]
    lottery(s,p,a,b,x)


