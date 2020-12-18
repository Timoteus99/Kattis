vnos = input().split()
prva_beseda = vnos[0]
druga_beseda = vnos[1]

# poiscemo crko, ki je skupna danima besedama
for crka in prva_beseda:
    if crka in druga_beseda:
        iskana_crka = crka
        mesto_prva = prva_beseda.index(iskana_crka) # za nadaljevanje naloge moramo določiti tudi indeks, kjer se crka nahaja
        break

mesto_druga = druga_beseda.index(iskana_crka)
    
kje_vr = 0
while kje_vr < len(druga_beseda): # pisemo n*m tabelo, kjer vrstice sestavljajo pike in znak iz druge besede
    kje_st = 0
    if kje_vr == mesto_druga:
        print(prva_beseda)
    else:
        niz = ''
        while kje_st < len(prva_beseda): # stolpce pa sestavljajo pike in znak iz prve besede
            if kje_st == mesto_prva:
                niz += druga_beseda[kje_vr]
            else:
                niz += '.'
            kje_st += 1
            
        print(niz)
        niz = ''
    
    kje_vr += 1