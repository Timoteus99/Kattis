stevilo_his = int(input())
niz = input()

zap_st = 1
tab = []
# zaporedna števila sproti dodajamo v tabelo
# če je znak enak 'R', pa števila v tabeli v nasprotni smeri izpišemo
# in izpraznimo tabelo
for smer in niz:
    tab.append(zap_st)
    if smer == 'R':
        for st in tab[::-1]:
            print(st)
        tab = [] #tabelo izpraznimo
    zap_st += 1
# na koncu nam ostane še zadnje število, oziroma zadnja tabela števil,
# če so bili pred tem v nizu 'L'-ji, tudi te izpišemo v obratni smeri.
tab.append(zap_st)
for st in tab[::-1]:
    print(st)



        
        
