N = list(map(int, input().split()))

ans = 0
for i in range(len(N)):
    ans += N[i]
print(ans)