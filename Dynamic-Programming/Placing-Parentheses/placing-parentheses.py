#uses python3

import sys
import numpy as np

def oper(a,b,op):
    if op == '+':
        return a + b 
    if op == '-':
        return a - b 
    if op == '*':
        return a*b

def maxval(digs,ops):
    n = len(digs)
    M = np.zeros((n,n))
    m = np.zeros((n,n))
    for i in range(0,n):
        M[i,i] = digs[i]
        m[i,i] = digs[i]
    for s in range(1,n):
        for j in range(s,n):
            i = j-s
            maxk = oper(M[i,j-1], M[j,j], ops[j-1])
            mink = oper(M[i,j-1], M[j,j], ops[j-1])
            for k in range(1,s+1):
                a = oper(M[i,j-k], M[j-k+1,j], ops[j-k])
                b = oper(M[i,j-k], m[j-k+1,j], ops[j-k])
                c = oper(m[i,j-k], M[j-k+1,j], ops[j-k])
                d = oper(m[i,j-k], m[j-k+1,j], ops[j-k])
                maxk = max(maxk,a,b,c,d)
                mink = min(mink,a,b,c,d)
            M[i,j] = maxk
            m[i,j] = mink
    return int(M[0,n-1])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(input)
    digs = data[0::2]
    ops = data[1::2]
    print(maxval(digs,ops))


