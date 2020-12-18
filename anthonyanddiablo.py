# program nam pove ali lahko z določeno dolžino obsega
# "obdamo" željeno ploščino

import math
podatka = input()
tab_podatkov = podatka.split()
A = float(tab_podatkov[0]) # zeljena ploscina lika
N = float(tab_podatkov[1]) # dolzina možnega obsega

# ker ima krog največjo ploščino glede na obseg
# za ploscino vzamemo ploščino kroga
r = N / (2 * math.pi) # izpeljemo iz formule za obseg kroga (r = polmer)
ploscina = math.pi * (r**2)

if ploscina >= A:
    print('Diablo is happy!')
    
# nima dovolj materiala...
else:
    print('Need more materials!')
    