#uses python3

import sys

def get_majority(n,a):
    list.sort(a)
    count = 1 
    for i in range(n-1):
        if a[i] == a[i+1]:
            count += 1
            if count > n/2:
                return 1
        else:
            count = 1 
    return 0

    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int,input.split()))
    n = data[0]
    a = data[1:]
    print(get_majority(n,a))
