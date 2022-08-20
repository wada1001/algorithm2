N = int(input())
A = list(map(int, input().split()))

# 100, 200, 300, 400
counts = [0, 0, 0, 0]

for i in A:
    counts[int(i / 100) - 1] += 1
print(counts[0] * counts[3] + counts[1] * counts[2])