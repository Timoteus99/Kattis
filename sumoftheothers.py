import sys
for vhodni_podatki in sys.stdin:
    #uporabljam sys.stdin, ker ne vem koliko podatkov je potrebno prebrati
    #vem samo da je potrebno brati iz standardnega vhoda
    seznam_stevil = list(map(int, vhodni_podatki.split()))
    #iz vhodnih podatkov naredim tabelo celih števil
  
    for kandidat in seznam_stevil:
        #kandidat je tisti, ki predstavlja vsoto vseh ostalih v tabeli
        #razen samega sebe, zato ga moram odšteti
        if sum(seznam_stevil)- kandidat == kandidat:
            print(int(kandidat))
            break #če sem najdla pravega kandidata zanko prekinem
    