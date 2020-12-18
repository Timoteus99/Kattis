import sys
mnozica_besed = set()
for vrstica in sys.stdin:
    nov_niz = ''
    for beseda in vrstica.split():
    #vse crke spremenim v male črke
        beseda = beseda.lower()
        if beseda in mnozica_besed:
            nov_niz += ' .' #zamik pred  piko, ker v izhodni vrstici mora bit
        else:
        #v primeru da besede še nimamo v mnozici besed jo bomo dodali
        #in tudi dodamo jo v naš niz
            mnozica_besed.add(beseda)
            nov_niz = nov_niz + ' ' + beseda
    print(nov_niz)

