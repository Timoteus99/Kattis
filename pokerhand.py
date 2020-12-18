#poker hand
slovar_kart = {}
karte = input().split(' ')
for el in karte:
    x = el[0] 
    #pogledamo, če smo na ta ključ že naleteli
    if x in slovar_kart.keys():
        slovar_kart[x] += 1
        #če smo, vrednost povečamo za 1
    else:
        slovar_kart.update({x : 1}) # doda kljuc, če ga se ni

maksimalno_st_istih = 0
for vrednost in slovar_kart:
    if int(slovar_kart[vrednost]) > maksimalno_st_istih: 
        maksimalno_st_istih = slovar_kart[vrednost]
        #najdemo največjo vrednost in jo izpišemo

print(maksimalno_st_istih)
    
