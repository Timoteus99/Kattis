#vnos spremenimo v seznam števil
vnos = list(map(int, input().split()))
#označimo ustrezne indekse vnosov
m = int(vnos[0])
a = int(vnos[1])
b = int(vnos[2])
c = int(vnos[3])
vsota = a + b + c
if vsota <= 2*m: #m pomnožimo z 2 zato, ker dva lahko izbereta isto jed
    print("possible")
else:
    print("impossible")