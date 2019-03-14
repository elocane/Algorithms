# uses python3

def gcd(a,b):
    while b!=0:
        b2 = a % b
        a = b
        b = b2
    return a;
    
def lcm(a,b):
    m = int((a//gcd(a,b))*b)
    return m;

inp = input().split()
a = int(max(inp))
b = int(min(inp))
print(lcm(a,b))
