N, S = list(map(int, input().split()))
res = 0
for num in range(1, N + 1):
    for num2 in range(1, N + 1):
        if num + num2 <= S:
            res += 1
print(res)