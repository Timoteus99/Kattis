def vsota(tab, m):
    '''vrne nam največjo možno vsoto števil podmnožice v dani tabeli števil'''
    delna_vsota = 0
    koliko_m = 0
    indeks_m = 0
    naj_vsota = 0
    kje = 0
    while True:
        # ko pregledamo celotno tabelo, smo našli največjo vsoto 
        if kje >= len(tab):
            break
        delna_vsota = 0
        indeks_m = 0
        koliko_m = 0
        while kje < len(tab):
            el = tab[kje]
            if el < m:
                # če je trenutno število manjše od 'm' moramo podmnožico zapreti
                # saj v njej ne sme biti manjšega število 
                if koliko_m == 0:
                    delna_vsota = 0
                kje += 1
                break
            # v nasprotnem primeru, vsoti prištejemo trenutno število
            # paziti moramo le še v primeru, da je število enako 'm'
            delna_vsota += el
            if el == m:
                koliko_m += 1
                if koliko_m == 1:
                    indeks_m = kje + 1
                    # zabeležimo si indeks kjer je stevilo 'm', saj moramo od tam nadaljevati
                    # ko pridemo do drugega 'm'-ja
                elif koliko_m == 2:
                    delna_vsota -= m
                    kje = indeks_m
                    # delno vsoto zmanjšano in gremo na prej označeno mesto
                    break
            kje += 1
        # vsakič pogledamo če smo morda našli novo največjo vsoto        
        if delna_vsota > naj_vsota:
            naj_vsota = delna_vsota
                
    return naj_vsota
        
koliko = int(input())
for podatki in range(koliko):
    prva_podatka = list(map(int,input().split()))
    n = prva_podatka[0]
    m = prva_podatka[1]
    zaporedje = list(map(int, input().split()))
    print(vsota(zaporedje, m))