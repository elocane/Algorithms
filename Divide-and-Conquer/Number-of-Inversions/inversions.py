#uses python3

import sys

count = 0

def merge_sort(n,a):
    if n == 1:
        return a[0:]
    k = n // 2
    l1 = merge_sort(k,a[0:k])
    l2 = merge_sort(n-k,a[k:])
    res = merge(l1,l2)
    return res
    
def merge(l1,l2):
    global count
    res = list()
    while (len(l1) != 0) & (len(l2) != 0):
        if l1[0] <= l2[0]:
            res.extend([l1[0]])
            l1.remove(l1[0])
            #print(res)
        else:
            res.extend([l2[0]])
            l2.remove(l2[0])
            count += len(l1)
    if len(l1) != 0:
        list.extend(res,l1[:])
    if len(l2) != 0:
        list.extend(res,l2[:])
    return res


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int,inp.split()))
    n = data[0]
    a = data[1:]
    merge_sort(n,a)
    print(count)
