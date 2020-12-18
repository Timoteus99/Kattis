def obrniStevilo(n):
    '''obrne dano stevilo'''
    stevilo = str(n)
    kje = len(stevilo) - 1
    obrnjeno = ''
    while kje >= 0:
        stevka = stevilo[kje]
        obrnjeno += stevka
        kje -= 1
    return obrnjeno

def jePalindrom(n):
    '''vrne True, ce je stevilo palidrom in False, ce ni'''
    if str(n) == obrniStevilo(n):
        return True
    else:
        return False

stStevil = int(input())
tab_stevil = []
for st in range(stStevil):
    stevilo = int(input())
    tab_stevil.append(stevilo)
    
for stevilo in tab_stevil:
    if jePalindrom(stevilo):
        print(str(stevilo))
    else:
        i = 1
        while True: 
            if jePalindrom(stevilo - i) and len(str(stevilo - i)) == 6:
                print(str(stevilo - i))
                break
            
            if jePalindrom(stevilo + i) and len(str(stevilo + i)) == 6:
                print(str(stevilo + i))
                break
            
            i += 1