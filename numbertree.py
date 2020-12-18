podatka = input().split()
st = int(podatka[0])
stevilo = 0

# določimo največje število
for i in range(st + 1):
    stevilo += 2 ** i
    
# ce v vnosu ni ukazov za premikanje po drevesu, vrnemo kar prvo število    
if len(podatka) == 1:
    print(stevilo)
else:
    niz = podatka[1]
    razlika = 1 
    
    for znak in niz:
        if znak == 'L':
            razlika += razlika
        else:
            razlika += razlika + 1 # če je ukaz v desno moramo odšteti mesto + 1
            
    # rezultatu pristejemo 1, saj smo prvo razliko (zato da se lahko pristeva)
    # nastavili na 1 namesto na 0
    print(stevilo - razlika + 1)
        
        