N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    ans += A[i][1] / A[i][0]
print(ans)