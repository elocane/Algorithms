#uses python3
import sys

def compare(a,b):
    ab = int(a+b)
    ba = int(b+a)
    if ab>=ba:
        return a
    else:
        return b
    

def largest(n,numbers):
    result = []
    while len(numbers) != 0:
        current = numbers[0]
        for i in range(n):
            current = compare(current,numbers[i])
        result += current
        numbers.remove(current)
        n -= 1
    print(*result,sep='')


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(str,input.split()))
    n = int(data[0])
    numbers = data[1:]
    largest(n,numbers)
