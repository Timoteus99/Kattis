a, b = input().split()

A = int(str(a)[::-1])
B = int(str(b)[::-1])

if A > B:
    print(A)
else:
    print(B)