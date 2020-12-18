koliko = int(input().split()[0])
tab = []
for vr in range(koliko):
    tab.append(list(input()))
tocka_vode = []
tocka_cilja = []
tocka_zacetka = []
tocka_kamnov = []
# določimo kje so posamezni elementi(naredimo graf):
x_ko = 0
y_ko = 0
kje = [x_ko, y_ko]
for el1 in tab:
    kje[0] = 0
    for el2 in el1:
        if el2 == 'D':
            tocka_cilja = [kje[0], kje[1]]
        elif el2 == 'S':
            tocka_zacetka.append([kje[0], kje[1]])
        elif el2 == '*':
            tocka_vode.append([kje[0], kje[1]])
        elif el2 == 'X':
            tocka_kamnov.append([kje[0], kje[1]])  
        kje[0] += 1
    kje[1] += 1

koliko = 1
# dokler ne pridemo, do cilja, ali pa nas 'zalije voda' spreminjamo zacetno matriko
# tako kot se posamezni elementi lahko prestavljajo
while True:
    # ce nas voda poplavi (v matriki ni vec S-jev) zapustimo zanko in izpisemo KAKTUS
    konec = True
    for vr in tab:
        if 'S' in vr:
            konec = False
            break
    if konec:
        print('KAKTUS')
        break     
    for tocka in tocka_zacetka:
        zacetek_x = tocka[0]
        zacetek_y = tocka[1]
        cilj_x = tocka_cilja[0]
        cilj_y = tocka_cilja[1]
        # poizkusimo vse poti - naredimo vse pomike ki jih lahko
        # (lahko jih v primeru, da je na sosednjih mestih '.' ali 'D', če je slednji, smo prišli na cilj) 
        try:
            if tab[zacetek_y][zacetek_x + 1] == '.':
                tab[zacetek_y][zacetek_x + 1] = 'S'
            elif tab[zacetek_y][zacetek_x + 1] == 'D':
                tab[zacetek_y][zacetek_x + 1] = 'S'
                print(koliko)
                break    
        except IndexError:
            pass # ce je indeks prevelik ne naredimo NIČ
        try:
            if tab[zacetek_y + 1][zacetek_x] == '.':
                tab[zacetek_y + 1][zacetek_x] = 'S'
            elif tab[zacetek_y + 1][zacetek_x] == 'D':
                tab[zacetek_y + 1][zacetek_x] = 'S'
                print(koliko)
                break    
        except IndexError:
            pass
        try:
            if zacetek_x > 0:
                # če je 'koordinata x' = 0, je ne ne smemo odšteti, saj tako dobimo
                # zadnji element v tabeli (ki pa ga nočemo)
                if tab[zacetek_y][zacetek_x - 1] == '.':
                    tab[zacetek_y][zacetek_x - 1] = 'S'
                elif tab[zacetek_y][zacetek_x - 1] == 'D':
                    tab[zacetek_y][zacetek_x - 1] = 'S'
                    print(koliko)
                    break   
        except IndexError:
            pass
        try:
            if zacetek_y > 0:
                # če je 'koordinata y' = 0, je ne ne smemo odšteti, saj tako dobimo
                # zadnji element v tabeli (ki pa ga nočemo)
                if tab[zacetek_y - 1][zacetek_x] == '.':
                    tab[zacetek_y - 1][zacetek_x] = 'S'
                elif tab[zacetek_y - 1][zacetek_x] == 'D':
                    tab[zacetek_y - 1][zacetek_x] = 'S'
                    print(koliko)
                    break     
        except IndexError:
            pass 
    # če pridemo do cilja zapustimo zanko (če v matriki ni več 'D'-jev)
    prisli_na_cilj = True
    for vr in tab:
        if 'D' in vr:
            prisli_na_cilj = False
    if prisli_na_cilj:
        break

    for tocka in tocka_vode:
        # podobno kot za začetek naredimo tudi za vodo, le da '*' napišemo v primeru, da je
        # na sosednjih mestih '.' ali pa 'S'
        voda_x = tocka[0]
        voda_y = tocka[1]
        try:
            if tab[voda_y][voda_x + 1] == '.' or tab[voda_y][voda_x + 1] == 'S':
                tab[voda_y][voda_x + 1] = '*'
        except IndexError:
            pass
        try:
            if tab[voda_y + 1][voda_x] == '.' or tab[voda_y + 1][voda_x] == 'S':
                tab[voda_y + 1][voda_x] = '*'
        except IndexError:
            pass
        try:
            if voda_x > 0:
                if tab[voda_y][voda_x - 1] == '.' or tab[voda_y][voda_x - 1] == 'S':
                    tab[voda_y][voda_x - 1] = '*'
        except IndexError:
            pass
        try:
            if voda_y > 0:
                if tab[voda_y - 1][voda_x] == '.' or tab[voda_y - 1][voda_x] == 'S':
                    tab[voda_y - 1][voda_x] = '*'
        except IndexError:
            pass
    # vse spremenljivke nastavimo spet na prvotno stanje (razen tabele)
    # in jim priredimo trenutno stanje v tabeli
    x_ko = 0
    y_ko = 0
    kje = [x_ko, y_ko]
    tocka_vode = []
    tocka_cilja = []
    tocka_zacetka = []
    tocka_kamnov = []
    for el1 in tab:
        kje[0] = 0
        for el2 in el1:
            if el2 == 'D':
                tocka_cilja = [kje[0], kje[1]]
            elif el2 == 'S':
                tocka_zacetka.append([kje[0], kje[1]])
            elif el2 == '*':
                tocka_vode.append([kje[0], kje[1]])
            elif el2 == 'X':
                tocka_kamnov.append([kje[0], kje[1]])
            kje[0] += 1
        kje[1] += 1
    koliko += 1
