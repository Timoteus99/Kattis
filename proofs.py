def pravilno_sklepanje(stevilo_primerov):
    '''Funkcija vrne ''correct'', če je sklep pravilen,
        v nasprotnem pa vrstico v kateri se prvič pojavi napaka'''
    mnozica_sklepov = set()
    
    for i in range(stevilo_primerov):
        #preverimo po vseh vrsticah
        vrstica = input() 
        if vrstica[0] == '-':
            #ce je prvi znak v vrstici '-',
            #pomeni, da NI predpostavk
            #vse kar je na desni(sklep) od tega dodamo v množico
            mnozica_sklepov.add(vrstica[3:])
        else:
            #razdelimo vrstico na dva dela
            #(predpostavka na levi, sklep na desni)
            predpostavke, sklep = vrstica.split(' -> ')
            for predpostavka in predpostavke.split():
                #če so vse predpostavke že v množici
                #dodamo tudi sklep v množico
                if predpostavka in mnozica_sklepov:
                    mnozica_sklepov.add(sklep)
                else:
                    #vrnemo številko vrstice
                    #(i+1) ker smo začeli z 0
                    return i + 1
    return 'correct'

print(pravilno_sklepanje(int(input())))