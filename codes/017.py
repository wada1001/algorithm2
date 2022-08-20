def gcd(a, b):
    while a >= 1 and b >= 1:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    else:
        return a

def div(ab, gcd):
    return int(ab / gcd)

LEN = int(input())
N = list(map(int, input().split()))

s = div(N[0] * N[1], gcd(N[0], N[1]))
for n in range(2, LEN):
    s = div(s * N[n], gcd(s, N[n]))    
print(int(s))
