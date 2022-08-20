N = int(input())

ans = []
while N > 1:
    for i in range(2, N + 1):
        if i * i > N:
            ans.append(N)
            N = 0
            break
        if N % i == 0:
            ans.append(i)
            N = int(N / i)
            break
print(' '.join(map(str, ans)))