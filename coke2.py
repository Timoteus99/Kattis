def koliko_kovancev(kolicina, sl_kovancev, koliko):
    '''vrne koliko kovancev je potrebno vstaviti, da dobimo zeljeno kolicino'''
    
#     if tab[kolicina][kovanci5][kovanci10] > 0:
#         return tab[kolicina][kovanci5][kovanci10]
    if kolicina == 0:
        return 0

    kovanci1 = sl_kovancev[1]
    kovanci5 = sl_kovancev[5]
    kovanci10 = sl_kovancev[10]
    
    if kovanci10 > 0 and kovanci1 > 2:
        sl_kovancev[10] -= 1
        sl_kovancev[1] -= 3
        sl_kovancev[5] += 1
        koliko = min(koliko, 4 + koliko_kovancev(kolicina-1, sl_kovancev, koliko))        
    if kovanci10 > 0:
        sl_kovancev[10] -= 1
        sl_kovancev[1] += 2
        koliko = min(koliko, 1 + koliko_kovancev(kolicina - 1, sl_kovancev, koliko))
    if kovanci5 > 0 and kovanci1 > 2:
        sl_kovancev[5] -= 1
        sl_kovancev[1] -= 3
        koliko = min(koliko, 4 + koliko_kovancev(kolicina-1, sl_kovancev, koliko))
    if kovanci5 > 1:
        sl_kovancev[5] -= 2
        sl_kovancev[1] += 2
        koliko = min(koliko, 2 + koliko_kovancev(kolicina-1, sl_kovancev, koliko))
    if kovanci1 > 7:
        sl_kovancev[1] -= 8
        koliko = min(koliko, 8 + koliko_kovancev(kolicina-1, sl_kovancev, koliko))
    
    return koliko

sl_kovancev = {}
st_primerov = int(input())
koliko = 1000000
for vr in range(st_primerov):
    vnos = input().split()   
    sl_kovancev[1] = int(vnos[1])
    sl_kovancev[5] = int(vnos[2])
    sl_kovancev[10] = int(vnos[3])   
    kolicina = int(vnos[0])   
    print(koliko_kovancev(kolicina, sl_kovancev, koliko))