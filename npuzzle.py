# program nam pove število premikov ki jih moramo v tabeli narediti
# da bo tabela urejena po abecednem vrstnem redu

tab_podatkov = list()
koliko = 0
while koliko < 4:
    podatki = input()
    tab_podatkov.append(podatki)
    koliko += 1

# vhodne podatke imamo spravljenje v tabeli...
# na problem gledamo kot na 4 x 4 matriko:
vrstice = {'A':1,
           'B':1,
           'C':1,
           'D':1,
           'E':2,
           'F':2,
           'G':2,
           'H':2,
           'I':3,
           'J':3,
           'K':3,
           'L':3,
           'M':4,
           'N':4,
           'O':4
           }

stolpci = {'A':1,
           'B':2,
           'C':3,
           'D':4,
           'E':1,
           'F':2,
           'G':3,
           'H':4,
           'I':1,
           'J':2,
           'K':3,
           'L':4,
           'M':1,
           'N':2,
           'O':3
           }
vsota = 0
razdalja = 0
stevec_vr = 0
while stevec_vr < len(tab_podatkov):
    elt_vr = tab_podatkov[stevec_vr]
    stevec_st = 0
    while stevec_st < len(elt_vr): # pogledamo vsak ij-ti element matrike
        elt_st = elt_vr[stevec_st]
        if elt_st == '.':
            stevec_st += 1
            continue
        elif stevec_vr + 1 != vrstice[elt_st] or stevec_st + 1 != stolpci[elt_st]:
            razdalja = abs(stevec_vr + 1 - vrstice[elt_st]) + abs(stevec_st + 1 - stolpci[elt_st])
            vsota += razdalja
        # drugace vsebuje element pravo crko
        stevec_st += 1
    stevec_vr += 1
print(vsota)
    