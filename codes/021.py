n, r = list(map(int, input().split()))

x = 1
for i in range(r):
    x *= n - i

y = 1
for i in range(1, r + 1):
    y *= i
print(x // y)