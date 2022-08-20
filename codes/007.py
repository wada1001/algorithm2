N = list(map(int, input().split()))

res = 0
for num in range(1, N[0] + 1):
    if num % N[1] == 0 or num % N[2] == 0:
        res+=1
print(res)