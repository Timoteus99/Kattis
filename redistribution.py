def razporediPoIndeksih(tab):
    '''vrne novo tabelo, ki je dana tabela razporejena po indeksih'''
    indeksi = []
    while tab != len(tab) * [0]:
        zeljeni_i = tab.index(max(tab))
        indeksi.append(str(zeljeni_i + 1))
        tab[zeljeni_i] = 0
    return indeksi

st_ucilnic = int(input())
st_ucencev = list(map(int, input().split()))

najvec_ucencev = max(st_ucencev)
indeks_naj = st_ucencev.index(najvec_ucencev)

# ce je stevilo ucencev v najvecji ucilnici, večje od vsote vseh ostalih ucencev, razporejanje ni mogoče
if najvec_ucencev > sum(st_ucencev[:indeks_naj] + st_ucencev[indeks_naj + 1:]):
    print('impossible')
    
# drugace pa stevilo ucencev razporedimo od najvecjega do najmanjsega    
else:
    print(' '.join(razporediPoIndeksih(st_ucencev)))