# za vsak posamezen stolpec gremo od dna navzgor in iščemo ovire oz. jabolke
# če najdemo jabolko, jo premaknemo navzdol, če je le možno

#  vrstica = 0 predstavlja vrh

def gravitacija(vrstica, stolpec, mreza):
    # ponavljamo dokler ne dosežemo vrha
    while vrstica > 0:
        # če najdemo ".", potem mora nekje nad to "." biti ali jabolko ali ovira, ali pa nič:
        if mreza[vrstica][stolpec] == '.':
            lokacija_nad_znakom = 0
            zgornja_vrstica = vrstica - 1
            # iz te trenutne vrstice iščemo navzgor kvadratke, dokler ne najdemo ovire, jabolke, ali vrha
            while True:
                # dosegli smo vrh
                if zgornja_vrstica < 0:
                    return
                if mreza[zgornja_vrstica][stolpec] == '#':
                    # najdena ovira, nastavimo "vrstica" (trenutno lokacijo) na lokacijo takoj nad to oviro
                    # torej prestavimo se nad oviro, in potem tam nadaljujemo enak postopek
                    vrstica = zgornja_vrstica - 1
                    break
                elif mreza[zgornja_vrstica][stolpec] == 'a':
                    # najdemo jabolko
                    # ker smo začeli iskati iz praznega polja in ni bilo drugih ovir do sedaj,
                    # vemo da se bo morala prestaviti navzdol
                    # torej nastavimo trenutno polje na "."
                    mreza[zgornja_vrstica][stolpec] = '.'
                    # jabolko pa premaknemo v polje, s katerega smo začeli iskanje
                    # (torej tisti prvi mreza[vrstica][stolpec] == '.' na začetku funkcije)
                    # + dodamo zamik za vsako jabolko, ki smo jo do zdaj že prestavili navzdol (to predstavlja spremenljivko 'lokacija_nad_znakom')
                    mreza[vrstica - lokacija_nad_znakom][stolpec] = 'a'
                    lokacija_nad_znakom += 1
                # prestavimo začasni kazalec na naslednji kvadratek
                zgornja_vrstica -= 1
        else:
            # če ni ".", potem enostavno gremo na naslednji znak
            vrstica -= 1

# preberemo vrstico in ločimo obe števili
vhodni_podatek = input().split()
stevilo_vrstic = int(vhodni_podatek[0])
stevilo_stolpcev = int(vhodni_podatek[1])

# preberemo eno po eno vrstico in sestavimo tabelo
mreza = []
for vrstica in range(stevilo_vrstic):
    # preberemo vrstico in z "list()" zapišemo vsak znak v stringu v svoj element v seznamu
    #naredimo tabelo tabel
    mreza.append(list(input()))

# sedaj pa za vsak posamezni stolpec odsimuliramo zadevo
for i in range(stevilo_stolpcev):
    # začnemo z najnižjo vrstico (stevilo_vrstic-1) in gremo navzgor
    gravitacija(stevilo_vrstic - 1, i, mreza)

# končen izpis
for vrstica in mreza:
    # pretvorimo seznam posameznih znakov nazaj v niz, da ga lahko normalno izpišemo
    izpis = ''.join(znak for znak in vrstica)
    print(izpis)

