
def vsota_stevk(n):
    '''vrne vsoto stevk danega stevila'''
    tab = list(str(n))
    vsota = 0
    for stevka in tab:
        vsota += int(stevka)
    return vsota

# program poisce minimalno in maksimalno stevilo med L in D
# katerega vsota stevk je enaka X

tab_podatkov = []
koliko = 0
while koliko < 3:
    podatki = input()
    tab_podatkov.append(podatki)
    koliko += 1

# imamo tabelo, sestavljeno iz vnosov oz. podatkov    
L = int(tab_podatkov[0])
D = int(tab_podatkov[1])
X = int(tab_podatkov[2])

prva_st = 0
druga_st = 0

for N in range(L, D + 1):
    if vsota_stevk(N) == X:
        prva_st = N
        break
# nasli smo najmanjse oz. minimalno stevilo...

for M in range(D, L - 1, -1):
    if vsota_stevk(M) == X:
        druga_st = M
        break
# nasli smo tudi najvecje oz. maksimalno stevilo
        
        
print('{0}{1}{2}'.format(prva_st,'\n',druga_st))