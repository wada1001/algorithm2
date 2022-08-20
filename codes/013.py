N = int(input())

for i in range(1, N + 1):
    if i * i >= N:
        break
    if N % i != 0:
        continue
    print(i)
    if N / i != i:
        print(int(N / i))