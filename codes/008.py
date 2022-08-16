A = list(map(int, input().split()))

N = A[0] + 1
S = A[1]

res = 0
for num in range(1, N):
    for num2 in range(1, N):
        if num + num2 <= S:
            res += 1
print(res)