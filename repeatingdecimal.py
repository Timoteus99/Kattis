import sys

def deli_stevili(a, b, c):
    '''Funkcija "peš" deli tuji si števili 'a' in 'b' in izpise 'c' decimalk'''
    rezultat = '0.' #saj je a<b
    for i in range(c):
        a = 10 * a
        decimalka = a // b
        a = a % b
        rezultat = rezultat + str(decimalka)
    return rezultat

for vrstica in sys.stdin:
    #iz vhodnih podatkov naredimo tabelo celih števil
    vrstica = list(map(int, vrstica.split()))
    izpis = deli_stevili(vrstica[0], vrstica[1], vrstica[2])
    print(izpis)
    