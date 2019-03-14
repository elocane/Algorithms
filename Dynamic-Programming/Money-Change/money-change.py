#uses python3

import sys

def change_recursive(n,denomins):
    for i in range(len(denomins)):
        if n == denomins[i]:
            return 1
    numb = n
    for i in range(len(denomins)):
        if n > denomins[i]:
            curr = change(n-denomins[i],denomins)
            if curr + 1 < numb:
                numb = curr + 1
    return numb

def change(n,denomins):
    mincoins = [n]*(n+1)
    mincoins[0] = 0
    for m in range(n+1):
        for j in range(len(denomins)):
            if m >= denomins[j]:
                numb = mincoins[m-denomins[j]] + 1
                if numb < mincoins[m]:
                    mincoins[m] = numb
    return mincoins[n]
    

if __name__ == '__main__':
    n = int(sys.stdin.read())
    denomins = [1,3,4]
    print(change(n,denomins))
