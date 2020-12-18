
def prestej1(zacetek, konec, niz):
    '''prešteje število "Z"-jev v danem nizu, če je podan začetek negativen'''
    prvi = niz[zacetek:].count('Z')
    drugi = niz[:konec+1].count('Z')
    spanje = prvi + drugi
    return spanje

def prestej(zacetek, konec, niz):
    '''prešteje število "Z"-jev v danem nizu, če je podan začetek pozitiven'''
    spanje = niz[zacetek:konec+1].count('Z')
    return spanje

podatki = input().split()
n = int(podatki[0])
p = int(podatki[1])
d = int(podatki[2])

niz = input()

utrujenost = 0
zacetek = -p + 1 # formula podana v navodilih
konec = 0

# posebej za prvi primer, da določimo začetek in konec 
if zacetek < 0:
    spanje = prestej1(zacetek, konec, niz)
else:
    spanje = prestej(zacetek, konec, niz)
st_spanj = spanje

if st_spanj < d:
    utrujenost += 1
zacetek += 1
   
# nato gledamo samo prvi in zadnji clen niza (koliko Z-jev pridobimo in
# koliko jih izgubimo)
for i in range(1, n):
    konec = i
    if niz[zacetek - 1] == 'Z':
        if st_spanj != 0: # 'število spanj' nemore biti negativno
            st_spanj -= 1
    if niz[konec] == 'Z':
        st_spanj += 1

    if st_spanj < d: # vsakič pogledamo kako je z utrujenostjo
        utrujenost += 1
    zacetek += 1
print(utrujenost)