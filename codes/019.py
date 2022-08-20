N = int(input())
A = list(map(int, input().split()))

counts = {1:0, 2:0, 3:0}
for i in A:
    counts[i] += 1

ans = 0
for v in counts.values():
    ans += int(v * (v - 1) / 2)
print(ans)