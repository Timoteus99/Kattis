n = int(input())

# preberemo n vrstic
for stevilka_vrstice in range(n):
    vrstica = input()

    # ustvarimo začetni seznam vseh podnizov, ki jih iščemo
    tab_nizov = []
    tab_nizov.append("w")
    tab_nizov.append("we")
    tab_nizov.append("wel")
    tab_nizov.append("welc")
    tab_nizov.append("welco")
    tab_nizov.append("welcom")
    tab_nizov.append("welcome")
    tab_nizov.append("welcome ")
    tab_nizov.append("welcome t")
    tab_nizov.append("welcome to")
    tab_nizov.append("welcome to ")
    tab_nizov.append("welcome to c")
    tab_nizov.append("welcome to co")
    tab_nizov.append("welcome to cod")
    tab_nizov.append("welcome to code")
    tab_nizov.append("welcome to code ")
    tab_nizov.append("welcome to code j")
    tab_nizov.append("welcome to code ja")
    tab_nizov.append("welcome to code jam")

    # v "stevilo_ponovitev" hranimo, kolikokrat se je ponovil posamezen niz iz "tab_nizov"
    stevilo_ponovitev = {}
    for niz in tab_nizov:
        # "niz" je tukaj en od zgornjih nizov ("w", "wel", "welcome t", ...)
        #vse ponovitve nastavi na 0, kljuci so nizi vrednosti so 0
        stevilo_ponovitev[niz] = 0

    # za vsako crko v vrstici:
    for crka in vrstica:
        # ponovimo tolikokrat, kolikor imamo nizov v "tab_nizov" (i = zaporedno število niza)
        for i in range(len(tab_nizov)):
            # če je znak enak zadnjemu znaku v trenutnem nizu
            # torej če je i = 3 in tab_nizov[i] = "wel", primerjamo crko z "l"
            if crka == tab_nizov[i][-1]:
                if i == 0:
                    # če je to čisto prvi niz ("w"), potem samo prištejemo +1
                    stevilo_ponovitev[tab_nizov[i]] += 1
                else:
                    # če ni prvi niz, potem prištejemo, kolikokrat se je ponovil prejšnji niz
                    # (torej tisti niz, ki ima eno črko manj)
                    stevilo_ponovitev[tab_nizov[i]] += stevilo_ponovitev[tab_nizov[i-1]]

    # vzamemo skupno število, kolikokrat se je ponovil celoten niz (zadnji element dobimo z [-1])
    skupna_vsota_ponovitev = stevilo_ponovitev[tab_nizov[-1]]

    # dokler je število daljše od 4 znake, odstrani levi znak
    izpis_rezultata = str(skupna_vsota_ponovitev)
    while len(izpis_rezultata) > 4:
        izpis_rezultata = izpis_rezultata[1:]

    # napiši toliko "0" pred število, da bodo na koncu 4 znaki
    while len(izpis_rezultata) < 4:
        izpis_rezultata = '0' + izpis_rezultata

    print("Case #", stevilka_vrstice + 1, ": ", izpis_rezultata, sep='')
