import math

N, W, H = input().split()
diag = math.sqrt(int(W) ** 2 + int(H) ** 2)
sez = []
for element in range(int(N)):
    vnos = int(input())
    sez.append(vnos)
for element in sez:
    if element <= diag:
        print('DA')
    else:
        print('NE')