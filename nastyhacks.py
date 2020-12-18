stevilo_primerov = int(input())
#z zanko for se bomo sprehodili po vseh vrsticah oziroma testnih primerih
for primer in range(stevilo_primerov):
    #vhodne podatke spremenimo v cela števila, ločena s presledkom
    brez_oglasevanja, oglasevanje, stroski_oglasevanja = map(int, input().split())
    #Da bi lahko naredili primerjavo, moramo profitu,
    #ki ga dobimo z oglaševanjem odšteti stroške oglaševanja
    razlika = oglasevanje - stroski_oglasevanja
    if brez_oglasevanja == razlika:
        print('does not matter')
    elif brez_oglasevanja < razlika:
        print('advertise')
    else:
        print('do not advertise')