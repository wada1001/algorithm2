def is_prime(a):
    for i in range(2, a):
        if i * i > a:
            break
        if a % i == 0:
            return False
    return True

N = int(input())

if is_prime(N):
    print("Yes")
else:
    print("No")