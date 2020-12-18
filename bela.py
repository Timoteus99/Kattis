# za vsako karto določimo njeno vrednost 
vr_dominantnih = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7':0}
vr_nedominantnih = {'A':11, 'K':4, 'Q':3, 'J':2, 'T':10, '9':0, '8':0, '7':0}

# program sesteje vsoto vrednosti vseh kart na mizi
# pri tem uposteva dominantnost karte

prva_vr = input().split()
dominantna = prva_vr[1]

st_rok = int(prva_vr[0]) # ena roka pomeni stiri karte
vsota = 0
koliko = 0
while koliko < st_rok * 4:
    podatek = input()
    # pregledamo vsak vnos posebej
    vrednost = podatek[0]
    barva = podatek[1]
    if barva == dominantna:
        vsota += vr_dominantnih[vrednost]
    else:
        vsota += vr_nedominantnih[vrednost]
    koliko += 1
# vsem kartam smo določilo vrednosti in jih sešteli...    
print(vsota)
