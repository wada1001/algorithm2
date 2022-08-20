A = list(map(int, input().split()))

ans = 1
for i in range(len(A)):
    ans *= A[i]
print(ans)