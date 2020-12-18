def sodaLiha(st_zamenjav):
    '''doloci sodost oz lihost'''
    urejen_niz = []
    # nastavimo si prvo vrednost glede na stevilo zeljenih zamenjav
    if st_zamenjav % 2==0:
        urejen_niz.append(0)
        prejsni = 0
    else:
        urejen_niz.append(1)
        prejsni = 1
        
    return (urejen_niz, prejsni)

def trdiDisk(dolzina, urejen_niz, prejsni, st_zamenjav, indeksi_pokv):
    '''sestavi tabelo enic in ničel, ki predstavljejo željen trdi disk'''
    stevec = 0
    i = 0
    for znak in range(2, dolzina+1):
        # ce smo prisli do zeljene količine zamenjav, dodamo na konec niza same nicle
        if stevec == st_zamenjav:
            urejen_niz.extend([0] * (dolzina - (znak-1)))
            break # zaključimo, ker imamo rešitev
        else:
            # sicer ugotaljamo ali je trenutni bit pokvarjen (0) ali ne... glede na to jih zapisujemo v tabelo
            # ter sproti štejemo 'bitne spremembe'
            if znak == indeksi_pokv[i]:
                urejen_niz.append(0)
                i += 1
                if prejsni == 1:
                    stevec += 1
                prejsni = 0
            # dodajamo nasprotne si vrednosti, dokler ne pridemo do zadostnega števila zamenjav
            else:
                if prejsni == 0:
                    urejen_niz.append(1)
                    prejsni = 1
                else:
                    urejen_niz.append(0)
                    prejsni = 0
                # v obeh primerih se zgodi 'bitna sprememba'
                stevec += 1
    return urejen_niz  

prva_vr = input().split()
dolzina = int(prva_vr[0])
st_zamenjav = int(prva_vr[1])
st_pokvarjenih = int(prva_vr[2])

indeksi_pokv = list(map(int, input().split()))

urejen_niz = sodaLiha(st_zamenjav)[0]
prejsni = sodaLiha(st_zamenjav)[1]
rez = list(map(str, trdiDisk(dolzina, urejen_niz, prejsni, st_zamenjav, indeksi_pokv)))
print(''.join(rez))


    
    