#Uses python3
import sys
import math

def min_dist(n, x, y):
    if n == 2:
        return math.sqrt((x[0] - x[1])**2 + (y[0] - y[1])**2)
    if n < 2:
        return 10**20
    pts = list(zip(x,y))
    list.sort(pts, key = lambda x: x[1])
    seen = set()
    for element in pts:
        if element in seen:
            return 0
        seen.add(element)
    if x[1:] == x[:-1]:
        list.sort(y)
        dist = math.sqrt((y[0] - y[1])**2)
        for i in range(1,n-1):
            if math.sqrt((y[i] - y[i+1])**2) < dist:
                dist = math.sqrt((y[i] - y[i+1])**2)
        return dist
    xavg = sum(x)/n
    left = []
    right = []
    for i in range(n):
        if pts[i][0] >= xavg:
            list.append(left,pts[i])
        else:
            list.append(right,pts[i])
    xleft = [i[0] for i in left]
    yleft = [i[1] for i in left]
    xright = [i[0] for i in right]
    yright = [i[1] for i in right]
    minleft = min_dist(len(xleft),xleft,yleft)
    minright = min_dist(len(xright),xright,yright)
    mintot = min(minleft,minright)
    check = list()
    for i in range(n):
        if abs(pts[i][0] - xavg) <= mintot:
            list.append(check,pts[i])
    d = mintot
    for i in range(len(check)):
        for j in range(1,min(7,len(check)-i)):
            val = math.sqrt((check[i][0] - check[i+j][0])**2 + (check[i][1] - check[i+j][1])**2)
            if val < d:
                d = val
    return d
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(min_dist(n, x, y)))

