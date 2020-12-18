#Dobimo vse podatke v int-obliki
stevilo_ekip, ekipe_z_unicenimi, ekipe_z_rezervnimi = map(int,input().split())

manjkajo_kajaki = set(map(int, input().split()))
imajo_rezervo = set(map(int, input().split()))

#Pregledamo vse ekipe
for ekipa in range(1, stevilo_ekip + 1): 
    #ce ekipa nima rezervnega kajaka, naredimo naslednje
    if ekipa in manjkajo_kajaki:
        #preverimo, ali ekipa pred to ekipo ima rezervni kajak
        if (ekipa > 1) and (ekipa - 1) in imajo_rezervo:
            #ce ga ima, naj ga odda 
            imajo_rezervo.remove(ekipa - 1)
            #ta ekipa si ga sposodi in ga ne rabi več
            manjkajo_kajaki.remove(ekipa)
        #če od prejšnjih sosedov, nismo uspeli dobiti rezervega kajaka
        #preverimo ali ga ima naslednja ekipa in zadevo ponovimo
        elif (ekipa < stevilo_ekip) and (ekipa + 1) in imajo_rezervo:
            imajo_rezervo.remove(ekipa + 1)
            manjkajo_kajaki.remove(ekipa)
            
print(len(manjkajo_kajaki))  #koliko ekip ni uspelo pridobiti rezervnega kajaka
