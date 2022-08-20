N = int(input())
A = list(map(int, input().split()))

m = {}

for i in A:
    if i in m:
        m[i] += 1
    else:
        m[i] = 1

ans = 0
for k in m.keys():
    if k == 50000:
        ans += m[k] * (m[k] - 1) // 2
        m[k] = 0
        continue
    if 100000 - k in m:
        ans += m[100000 - k] * m[k]
        m[k] = 0
print(ans)