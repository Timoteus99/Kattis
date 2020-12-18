# program nam izpise "safe" pri t.i. varnem letu in
# izracuna razdaljo, ki jo bodo sani prevozile preden zadanejo tla pri
# nevarnem letu

import math
podatka = input()
tab_pod = podatka.split()

if int(tab_pod[1]) <= 180:
    print('safe')
    
else:
    # izracunamo diagonalo pravokotnega trikotnika, ki ga sestavljata
    # katete pri kotu 180 in 270 stopinj
    # ali pa katete pri kotu 270 in 360 stopinj
    kot = abs(int(tab_pod[1]) - 270)
    razdalja = int(tab_pod[0]) / math.cos(kot * math.pi/180)
    print(abs(int(razdalja)))
