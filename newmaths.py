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

def novo_množenje(stevilo):
    '''izračuna kvadrat števila po pravilu, ki upošteva novo seštevanje'''
    tab = []
    produkt = ''
    # največja možna dolžina produkta
    k = (len(stevilo) * 2) - 1
    
    # za lazje racunanje pred stevilo postavimo zadosto količino ničel
    koliko = k - len(stevilo)
    stevilo = '0'*koliko + stevilo
    while stevilo != '':
        i = k - 1
        for stevka1 in stevilo:
            stevka2 = stevilo[i] 
            if int(stevka1) * int(stevka2) != 0:
                tab.append(str(int(stevka1)*int(stevka2)))
            i -= 1
        produkt += str(int(novo_seštevanje(tab)) % 10)
        stevilo = stevilo[1:]
        k -= 1
        tab = []
        
    return produkt

st = int(input())
dolzina = len(str(st))
obstaja = False

if dolzina % 2 == 0 or str(st)[-1] == '2' or str(st)[-1] == '3':
    print('-1')

else:
    koliko_mestno = (dolzina + 1) // 2

    for i in range(10**(koliko_mestno - 1), 10**(koliko_mestno)):
        if novo_množenje(str(i)) == str(st):
            print(str(i))
            obstaja = True
            break
    if not obstaja:
        print('-1')
    
    
            
            