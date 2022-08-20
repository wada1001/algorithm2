N, M = list(map(int, input().split()))

while N >= 1 and M >= 1:
    if N > M:
        N = N % M
    else:
        M = M % N
if N == 0:
    print(M)
else:
    print(N)
