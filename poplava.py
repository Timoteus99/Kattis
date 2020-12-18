
podatka = input().split()
stevilo_st = int(podatka[0])
prostornina = int(podatka[-1])

# to je najvec vode, ki jo premore histogram
naj_vode = (stevilo_st - 1) * (stevilo_st - 2) // 2

if naj_vode < prostornina or stevilo_st < 3: # histogram z dvema stolpcema ne more vsebovati vode 
    print('-1')

else:
    histogram = [str(stevilo_st)]
    dodatna_tab = []
    st_premikov = naj_vode - prostornina
    # program se hitreje odvije, ce prej definiramo .append spremenljivke
    dodaj_tab = dodatna_tab.append
    dodaj_hist = histogram.append
    drugi_naj = stevilo_st - 1
    
    for st in range(drugi_naj - 1, 0, -1):
        if st_premikov >= st:
            st_premikov -= st
            dodaj_tab(st)
        else:
            dodaj_hist(str(drugi_naj - st))
            
    dodaj_hist(str(drugi_naj))
    
    # imamo dve tabeli: v prvi(histogram) so visine stolpcev, ki dejansko naredijo prostor za
    # ustrezno količino vode
    # v drugi(dodatna_tab) pa so visine "odvečnih" stolpcev, slednje le še ustrezno pripisemo prvi tabeli...
    for st in range(len(dodatna_tab) - 1, -1, -1):
        dodaj_hist(str(drugi_naj - dodatna_tab[st]))
    
    print(' '.join(histogram))
     