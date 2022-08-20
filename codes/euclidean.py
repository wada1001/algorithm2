N = list(map(int, input().split()))

A = N[0]
B = N[1]

while A >= 1 and B >= 1:
    if A > B:
        A = A % B
    else:
        B = B % A

if A >= 1:
    print(A)
else:
    print(B)

