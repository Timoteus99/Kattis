kislo = [0 for _ in range(10)]
grenko = [0 for _ in range(10)]
best = 1000000000
def razlika(x, y):
    return abs(x - y)
def perket(i, kislost, grenkoba):
    global best
    if i == n:
        if grenkoba > 0 and razlika(kislost, grenkoba) < best:
            best = razlika(kislost, grenkoba)
    else:
        perket(i + 1, kislost, grenkoba)
        perket(i + 1, kislost * kislo[i], grenkoba + grenko[i])
n = int(input())
for i in range(n):
    vrstica = input()
    kislo[i], grenko[i] = map(int, vrstica.split(" "))
perket(0, 1, 0)
print(best)