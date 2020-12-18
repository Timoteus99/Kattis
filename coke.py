def stej10(sl_kovancev, kolicina):
    '''steje kolikokrat vrzemo v bankomat 10kron'''
    stevec = 0
    while sl_kovancev[10] > 0 and kolicina > 0:
        sl_kovancev[10] -= 1
        sl_kovancev[1] += 2
        stevec += 1
        kolicina -= 1
    return (stevec, kolicina)

def stej10_2(sl_kovancev, kolicina):
    '''steje kolikokrat vrzemo v bankomat 10kron in 1krono, ce jih imamo na razpolago'''
    stevec = 0
    while sl_kovancev[10] > 0 and sl_kovancev[1] > 2 and kolicina > 0:
        # ce imamo 1x10 in 3x1 krono moramo vsaviti vse, da nam bankomat vrne 5kron
        sl_kovancev[10] -= 1
        sl_kovancev[1] -= 3
        sl_kovancev[5] += 1
        stevec += 4
        kolicina -= 1
    return (stevec + stej10(sl_kovancev, kolicina)[0], kolicina) # dodamo preostanek, ce zmanjka kovancev po 1 krono

def stej5(sl_kovancev, kolicina):
    '''steje kolikokrat vrzemo v bankomat 5 kron'''
    stevec = 0
    while sl_kovancev[5] > 1 and kolicina > 0:
        sl_kovancev[5] -= 2
        sl_kovancev[1] += 2
        stevec += 2
        kolicina -= 1
    if sl_kovancev[5] == 1 and kolicina > 0:
        sl_kovancev[5] -= 1
        sl_kovancev[1] -= 3
        stevec += 4
        kolicina -= 1
    return (stevec, kolicina)

def stej5_2(sl_kovancev, kolicina):
    '''steje kolikokrat vrzemo v bankomat po 5 in 1 krono, dokler ene od teh ne zmanjka'''
    stevec = 0
    while sl_kovancev[5] > 0 and sl_kovancev[1] > 2 and kolicina > 0:
        sl_kovancev[5] -= 1
        sl_kovancev[1] -= 3
        stevec += 4
        kolicina -= 1
    return (stevec + stej5(sl_kovancev, kolicina)[0], kolicina)
    

def koliko_kovancev_1(sl_kovancev, kolicina):
    '''vrne najmanjse mozno stevilo kovancev, ki jih je potrebno vnesti da dobimo zeljeno količino kokakol'''
    stevec = 0
    rez = stej10(sl_kovancev, kolicina)
    stevec += rez[0]
    rez = stej5(sl_kovancev, rez[1])
    stevec += rez[0]
    stevec += rez[1] * 8
    return stevec

def koliko_kovancev_2(sl_kovancev, kolicina):
    '''vrne najmanjse mozno stevilo kovancev, ki jih je potrebno vnesti da dobimo zeljeno količino kokakol'''
    stevec = 0
    rez = stej10(sl_kovancev, kolicina)
    stevec += rez[0]
    rez = stej5_2(sl_kovancev, rez[1])
    stevec += rez[0]
    stevec += rez[1] * 8
    return stevec

def koliko_kovancev_3(sl_kovancev, kolicina):
    '''vrne najmanjse mozno stevilo kovancev, ki jih je potrebno vnesti da dobimo zeljeno količino kokakol'''
    stevec = 0
    rez = stej10_2(sl_kovancev, kolicina)
    stevec += rez[0]
    rez = stej5(sl_kovancev, rez[1])
    stevec += rez[0]
    stevec += rez[1] * 8
    return stevec

def koliko_kovancev_4(sl_kovancev, kolicina):
    '''vrne najmanjse mozno stevilo kovancev, ki jih je potrebno vnesti da dobimo zeljeno količino kokakol'''
    stevec = 0
    rez = stej10_2(sl_kovancev, kolicina)
    stevec += rez[0]
    rez = stej5_2(sl_kovancev, rez[1])
    stevec += rez[0]
    stevec += rez[1] * 8
    return stevec


st_primerov = int(input())
sl_kovancev = {}

for vr in range(st_primerov):
    vnos = input().split()
    kolicina = int(vnos[0])
    sl_kovancev[1] = int(vnos[1])
    sl_kovancev[5] = int(vnos[2])
    sl_kovancev[10] = int(vnos[3])
    
    sl_kovancev_1 = sl_kovancev.copy()
    sl_kovancev_2 = sl_kovancev.copy()
    sl_kovancev_3 = sl_kovancev.copy()
    sl_kovancev_4 = sl_kovancev.copy()
    print(min(koliko_kovancev_1(sl_kovancev_1, kolicina), koliko_kovancev_2(sl_kovancev_2, kolicina), koliko_kovancev_3(sl_kovancev_3, kolicina), koliko_kovancev_4(sl_kovancev_4, kolicina)))
    

        
            
            
        
    
    
            
    
    
    