def MinimalnaVsota(prvi_stolpec, drugi_stolpec):
    '''Kot argument dobi dve tabeli, ki prikazujeta stevilo posameznih stevil v vnosu.
       Funkcija vraca izračunano maksimalno vsoto para stevil, ki ga sestavlja doloceno stevilo
       iz prve in iz druge tabele, tako da je ta vsota minimalna.
    '''
    najmanjsi = 0
    najvecji = 100
    # stolpca bomo spreminjali (zmanjsevali vrednosti) zato si naredimo kopiji
    kopija1 = prvi_stolpec[:]
    kopija2 = drugi_stolpec[:]
    prazna_tab = False
    naj_vsota = 0
    while True:
        # vrednosti preglejujemo od najmanjše do največje
        while kopija1[najmanjsi] == 0:
            najmanjsi += 1
            if najmanjsi > 100:
                # pridemo do konca brez...
                # tabela je bila prazna (vse vrednosti so bile 0)
                prazna_tab = True
                break
            
        # enako pregejujemo tudi drugo tabelo, le da iz nasprotne smeri   
        while kopija2[najvecji] == 0:
            najvecji -= 1
            if najvecji < 0:
                prazna_tab = True
                break
            
        if prazna_tab:
            # če so bile obe tabeli prazni smo pregledali vse vsote
            break
        
        # drugače pa nastavimo novo največjo vsoto, ki je hkrati tudi najmanjša možna
        # saj smo povezovali največje (iz prve tabele) in najmanjše (iz druge tabele) vrednosti
        naj_vsota = max(naj_vsota, najmanjsi + najvecji)
        odstej = min(kopija1[najmanjsi], kopija2[najvecji])
        # da se znebimo ponavljajočim se številom, zmanjšamo vrednosti v tabeli
        # za manjšo izmed obeh trenutnih vrednosti
        kopija1[najmanjsi] -= odstej
        kopija2[najvecji] -= odstej
        
    return naj_vsota


koliko = int(input())
prvi_stolpec = 101 * [0]
drugi_stolpec = 101 * [0]
# podatke si shranjujemo tako, da povečujemo vrednosti indeksov v tabeli
# ker vemo, da imamo opravka s števili od 1 do 100
tab = []
dodaj = tab.append
for vnos in range(koliko):
    podatka = input().split()
    prvi_stolpec[int(podatka[0])] += 1
    drugi_stolpec[int(podatka[1])] += 1
    dodaj(MinimalnaVsota(prvi_stolpec, drugi_stolpec))

for vsota in tab:
    print(vsota)
