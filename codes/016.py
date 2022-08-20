N1 = int(input())
N = list(map(int, input().split()))

s = N[0]
for n in N[1:len(N)]:
    while n >= 1 and s >= 1:
        if s > n:
            s = s % n
        else:
            n = n % s
    if n >= 1:
        s = n
print(s)