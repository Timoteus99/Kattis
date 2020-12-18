def novo_seštevanje(tab):
    '''sesteje stevila v tabeli po pravilu, ki desetice ne prenaša (7+5=2)'''
    vsota = '0'
    for stevilo in tab:
        if len(vsota) < len(stevilo):
            razlika = len(stevilo) - len(vsota)
            vsota = '0'*razlika + vsota
        elif len(vsota) > len(stevilo):
            razlika = len(vsota) - len(stevilo)
            stevilo = '0'*razlika + stevilo
        nova_vsota = ''
        kje = 0
        for stevka in stevilo:
            nova_vsota += str((int(stevka) + int(vsota[kje])) % 10)
            kje += 1
        vsota = nova_vsota
        
    return vsota

def sistem_enačb(koliko_mestno, dolzina_produkta, kvadrat):
    '''izračuna sistem enačb'''
    st_nicelnih = dolzina_produkta - koliko_mestno
    stevilo = ['0']*st_nicelnih + ['x']*koliko_mestno
    produkt = ''

    while stevilo != '':
        i = st_nicelnih
        for stevka2 in stevilo:
            stevka1 = stevilo[i] 
            if stevka1 != '0' and stevka2 != '0':
                # za prvi primer
                if stevka1 == stevka2:
                    for st in range(10):
                        if st**2 % 10 == kvadrat[j]:
                            stevilo[i] = str(st)
                else:
                    
                    
                        
                        
                tab.append(str(int(stevka1)*int(stevka2)))
            i -= 1
        produkt += str(int(novo_seštevanje(tab)) % 10)
        stevilo = stevilo[1:]
        k -= 1
        tab = []
        
    return produkt