stevilo_nogavic, kapaciteta_stroja, max_barvna_razlika = map(int, input().split())

barve = sorted(list(map(int, input().split()))) # seznam moramo posortirati!!!

stevilo_pralnih_strojev, spodnja, zgornja = 0, 0, 0

if kapaciteta_stroja < stevilo_nogavic: # ce pogoj velja, vemo da bo zagotovo potreboval vec kot 1 pralni stroj
    while True:
        zgornja = spodnja + kapaciteta_stroja - 1 
        if stevilo_nogavic <= spodnja:  
            break 
        elif stevilo_nogavic <= zgornja:
            zgornja = stevilo_nogavic - 1 
        while spodnja <= zgornja:
            if abs(barve[spodnja] - barve[zgornja]) <= max_barvna_razlika: # |Di - Dj| <= K
                stevilo_pralnih_strojev += 1
                spodnja = zgornja + 1
                break #imamo nov pralni stroj, gremo iz zanke prepisemo zgornjega in preverimo ce je stevilo nogavic manjse/enako spodnjemu
            else:
                zgornja -= 1
    print(stevilo_pralnih_strojev)
else:
    print(1)