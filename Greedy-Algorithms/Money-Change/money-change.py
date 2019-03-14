#uses python3

def coins(m):
    n = m // 10
    n += (m % 10) // 5
    n += (m % 5)
    return n


m = int(input())
print(coins(m))
