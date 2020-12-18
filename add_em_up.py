def obrniStevilo(n):
    '''obrne stevilo'''
    obrnjena_st = [0, 1, 2, -1, -1, 5, 9, -1, 8, 6]
    obrnjeno = 0
    while n > 0:
        d = n % 10
        if obrnjena_st[d] == -1:
            return -1
        obrnjeno = obrnjena_st[d] + obrnjeno * 10
        n = n // 10
    return obrnjeno

def JeNotri(tab_stevil, zeljenaVsota, obrnjena):
    '''vrne ali je razlika v tabeli ali ne'''
    for st in tab_stevil:
        
        razlika = str(zeljenaVsota - int(st))
        kje = tab_stevil.index(st)
        kopija = tab_stevil[:kje] + tab_stevil[kje + 1:]
        kopija2 = obrnjena[:kje] + obrnjena[kje + 1:]
        
        if razlika in kopija2 or razlika in kopija:
            return True
        
        kopija = tab_stevil
        kopija2 = obrnjena
        
    return False

def JeNotriWhile(tab_stevil, zeljenaVsota, obrnjena):
    '''vrne ali je razlika v tabeli ali ne'''
    i = 0
    koliko_elementov = len(tab_stevil) - 1
    while i < koliko_elementov:
        razlika = str(zeljenaVsota - int(tab_stevil[i]))
#        kje = tab_stevil.index(tab_stevil[i])
        kopija = tab_stevil[:i] + tab_stevil[i + 1:]
        kopija2 = obrnjena[:i] + obrnjena[i + 1:]
        
        if razlika in kopija2 or razlika in kopija:
            return True
        i += 1
        
    return False


prvaVr = input().split()
kolikoSt = int(prvaVr[0])
zeljenaVsota = int(prvaVr[1])
tab_stevil = input().split()

obrnjena = []
#vsa = tab_stevil
for st in tab_stevil:
    if obrniStevilo(int(st)) != -1:
        obrnjena.append(str(obrniStevilo(int(st))))

if JeNotriWhile(tab_stevil, zeljenaVsota, obrnjena) or JeNotri(obrnjena, zeljenaVsota, tab_stevil):
#if JeNotriWhile(vsa, zeljenaVsota, obrnjena):
    print('YES')
else:
    print('NO')