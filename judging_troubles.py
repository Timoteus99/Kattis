
import collections

n = int(input())
sez_dom = []
sez_kat = []

for element in range(0, n):
    input_dom = str(input())
    sez_dom.append(input_dom)
stej_dom = collections.Counter(sez_dom)
#print(stej_dom)


for element in range(n, n * 2):
    input_kat = str(input())
    sez_kat.append(input_kat)
stej_kat = collections.Counter(sez_kat)
#print(stej_kat.values())
#print(min(stej_kat))

primerjaj = 0

#print(min([stej_kat, stej_dom], key = len))

for element in min([stej_kat, stej_dom], key = len):
    #print(stej_kat, stej_dom)
    primerjaj += min(stej_kat[element], stej_dom[element])
#print(stej_kat - stej_dom, stej_dom - stej_kat)
print(primerjaj)