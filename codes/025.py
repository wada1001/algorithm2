N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += A1[i] / 3 + A2[i] * 2 / 3
print(ans)