#NALOGA DATUM
#začnemo z četrtkom, ker je to 01.01.2020
dnevi_v_tednu = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
vpisni_podatki = input().split(' ')
dan = int(vpisni_podatki[0]) #ustrezna določitev indeksov vhodnih podatkov
mesec = int(vpisni_podatki[1])
#izpis števila dni v mescih iz leta 2009
meseci = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#vsota je število dni od 01.01.2009 do vpisanega datuma
vsota = sum(meseci[:mesec-1]) + (dan - 1)
x = vsota % 7 #ostanek pri deljenju z 7 nam bo dal ustrezen indeks

print(dnevi_v_tednu[x])
