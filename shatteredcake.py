sirina_torte = int(input())
stevilo_kosov = int(input())
celota = 0
for kos in range(stevilo_kosov):
    sirina_kosa, visina_kosa = map(int,input().split())
    #Uporabimo formulo za površino pravokotnih likov
    #površino vsakega kosa dodamo celotni povrsini
    celota += sirina_kosa * visina_kosa
print(celota // sirina_torte)