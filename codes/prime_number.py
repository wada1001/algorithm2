N = int(input()) 

is_prime = True
for p in range(2, N):
    if N % p == 0:
        is_prime = False
        break

if is_prime:
    print('prime')
else:
    print('composite')
