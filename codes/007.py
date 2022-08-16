A = list(map(int, input().split()))

res = 0
for num in range(A[0]):
    if num % A[1] == 0 or num % A[2] == 0:
        res+=1
print(res)