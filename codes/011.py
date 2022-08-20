def is_prime(a):
    for i in range(2, a):
        if i * i > a:
            break
        if a % i == 0:
            return False
    return True

N = int(input())

ans = []
for i in range(2, N + 1):
    if is_prime(i):
        ans.append(i)
print(' '.join(map(str, ans)))