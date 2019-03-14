#uses python3

import sys

def calculator(n):
    minsteps = [n]*(n+1)
    minsteps[0] = 0
    minsteps[1] = 0
    procedures = ['-1','0']
    for m in range(2,n+1):
        if m - 1 >= 1:
            numb = minsteps[m-1] + 1
            if numb < minsteps[m]:
                minsteps[m] = numb
                curr = '1'
        if m % 2 == 0 and m/2 >= 1:
            numb = minsteps[m//2] + 1 
            if numb < minsteps[m]:
                minsteps[m] = numb
                curr = '2'
        if m % 3 == 0 and m/3 >=1:
            numb = minsteps[m//3] + 1 
            if numb < minsteps[m]:
                minsteps[m] = numb
                curr = '3'
        list.append(procedures,curr)
    end = n
    k = n
    values = [n]
    while end > 1:
        if procedures[k] == '1':
            end = end - 1
            values.insert(0,end)
            k = k - 1
        if procedures[k] == '2':
            end = end//2
            values.insert(0,end)
            k = k//2
        if procedures[k] == '3':
            end = end//3 
            values.insert(0,end)
            k = k//3
    print(minsteps[n])
    print(*values,sep=' ')
    return 

if __name__ == '__main__':
    n = int(sys.stdin.read())
    calculator(n)


