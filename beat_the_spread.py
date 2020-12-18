stevilo_primerov = input()

ekipa_a, ekipa_b = 0, 0
for element in range(int(stevilo_primerov)):
    vsota, razlika = map(int, input().split())
    if razlika > vsota: #razlika ne sme biti vecja od vsote, to bi pomenilo, da je eden od njih negativen
        print("impossible")
    else:
        ekipa_a = (vsota + razlika) / 2 #sestevek vsote in razlike deljen z 2 je definicija ene ekipe oz rezultata
        if ekipa_a == int(ekipa_a): #vsota in razlika morata biti deljiva z 2
            ekipa_b = ekipa_a - razlika #druga ekipa ima torej rezultat ekipa_a - razlika
            maximum = int(max(ekipa_a, ekipa_b))
            minimum = int(min(ekipa_a, ekipa_b))
            print('{} {}'.format(maximum, minimum))
        else:
            print("impossible")