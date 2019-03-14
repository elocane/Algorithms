#uses python3
import sys
import numpy as np

def points(n,segments):
    m = 1
    pts = np.array([segments[0,1]])
    current = segments[0,1]
    for i in range(n):
        if (current < segments[i,0]):
            m += 1 
            current = segments[i,1]
            pts = np.append(pts,[segments[i,1]])
    print(m)
    print(*pts,sep=' ')



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = np.array(data[1::2])
    b = np.array(data[2::2])
    segments = np.column_stack((a,b))
    segments = segments[np.argsort(segments[:,1])]
    points(n,segments)
