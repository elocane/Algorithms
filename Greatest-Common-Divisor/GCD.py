#uses python3

inp = input().split()
a = int(max(inp))
b = int(min(inp))

while b!=0:
    b2 = a % b
    a = b
    b = b2

print(a)
