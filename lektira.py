def obrniBesedo(beseda):
    '''obre vrstni red črk v besedi'''
    return beseda[::-1]

def najdiPrvo(beseda):
    '''funkcija vrne niz, ki je najmanjsi po vrednosti glede mesta crk (kot v slovarju)'''
    prva = sorted(beseda)[0] # najprej poiscemo crko najmanjse vrednosti
    tab_mest = []
    indeks = 0
    # ce se ta crka pojavi na večih mestih moramo najti obratno obrnjen niz,
    # ki je najmanjsi po leksikografski vrednosti
    for crka in beseda:
        if crka == prva:
            tab_mest.append(indeks)
        indeks += 1
    
    tab_moznih = [] # poiščemo vse možne nize (nizi, ki se začnejo s črko najmanjše vrednosti)
    for mesto in tab_mest:
        tab_moznih.append(beseda[:mesto+1][::-1])    
    pravi_del = min(tab_moznih) # funkcija min nam poda niz, ki ga išemo
    return pravi_del


beseda = input()
# vemo da moramo dani niz razdeliti na 3 dele, zato vzamemo skrajsan niz (za 2 znaka)
prvi_del = najdiPrvo(beseda[:-2])
dolzina_prve = len(prvi_del)

drugi_del = najdiPrvo(beseda[dolzina_prve:-1])
dolzina_druge = len(drugi_del)

tretji_del = obrniBesedo(beseda[dolzina_prve + dolzina_druge:])

print(prvi_del + drugi_del + tretji_del)