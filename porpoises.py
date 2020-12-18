# Bistvo te naloge je, da je treba izračunati fibonaccijevo zaporedje,
# s tem da je treba odrezati vse vrednosti nad 10^9 ob vsakem posameznem "koraku" oz. zaporednem letu
import math
milijarda = 10**9

def razpakiraj_tuple(a, b):
    '''Omogočen izpis treh razpakiranih vrednosti.'''
    temp = a * a + b * b
    # vrnemo tri vrednosti - a*(b*2-a), temp in "odrezano" temp
    return (a * (b * 2 - a), temp, temp % milijarda)

def fibonacci(n):
    if n == 0:
        return (0, 1)
    else:
        # namesto da se računamo vsak korak oz. vsako leto posebej, izracunamo samo log n teh korakov (fib polovične vrednosti)
        # formula in razlaga: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html  #section3

        # rekurzivno znova pokličemo to funkcijo za (n / 2), jo razpakiramo z razpakiraj_tuple in dobimo tri vrednosti
        izracun = fibonacci(math.floor(n / 2))
        # vzamemo tri vrednosti iz tega rezultat
        # z * vrnemo "skupek" (tuple) treh vrednosti in "razpakiramo" v te tri spremenljivke a, b in c
        izracun = razpakiraj_tuple(*izracun)
        a = izracun[0]
        b = izracun[1]
        c = izracun[2]

        if n % 2 == 0:
            # če je n sodo število, potem:
            return (a % milijarda, c)
        else:
            # če je liho:
            return (c, (a + b) % milijarda)

n = int(input())
for _ in range(n):
    # preberemo vrstico in ločimo obe števili
    vhod = input().split()
    nabor_podatkov = int(vhod[0])
    zacetno_st_pliskavk = int(vhod[1])

    # izračunamo vrednost, in vzamemo le prvo število iz rezultata (torej ali "a % milijarda", ali pa "c" iz zadnjega returna)
    stevilo_parov = fibonacci(zacetno_st_pliskavk)[0]
    print(str(nabor_podatkov) + ' ' + str(stevilo_parov))