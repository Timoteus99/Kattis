# iščemo najdaljše nepretrgano zaporedje unikatnih številk
stevilo_testnih_primerov = int(input())

for primer in range(stevilo_testnih_primerov):
    # preberemo stevilo snezik v paketu
    stevilo_snezink = int(input())

    skatla= {}
    trenutno_nepretrgano_zaporedje = 0
    najdaljse_zaporedje = 0
    # preberemo toliko snezink, kot jih bi naj bilo v paketu
    for zap_st_snezinke in range(stevilo_snezink):
        snezinka = int(input())
        # v kolikor snežinke ni v škatli, prištejemo +1 k številu unikatnih snežink tega paketa in jo dodamo v škatlo
        if snezinka not in skatla:
            # zapisemo zaporedno st, kdaj se je nazadnje ponovila ta snezinka
            trenutno_nepretrgano_zaporedje += 1
        else:
            # tukaj sta dve možnosti, moramo pa vzeti najkrajšo
            # - trenutno_nepretrgano_zaporedje + 1
            # v primeru, da je trenutno zaporedje krajše od zadnje ponovitve te snežinke
            # recimo primer: 12321 - pri zadnji "1" je "tekoče zaporedje" enako 2 in ne 4

            # - z drugo možnostjo (zap_st_snezinke - skatla[snezinka]) ugotovimo, koliko snezink nazaj se je nazadnje zgodila ta snezinka
            # na tej točki nedvoumno vemo, da je "trenutno_nepretrgano_zaporedje" enako trenutni nepretrgani dolžini unikatnih snežnik
            # če iz trenutne zaporedne stevilke torej odštejemo, kdaj se je ta snežinka nazadnje zgodila,
            # vemo, kako dolgo je bilo zaporedje od zadnje ponovitve do sedaj
            # (primer: 1 1 2 2 - pri zadnji "2" je razdalja do prejšnje "2" enaka 1 - torej trenutno zaporedje je dolgo 1)

            trenutno_nepretrgano_zaporedje = min(trenutno_nepretrgano_zaporedje + 1, zap_st_snezinke - skatla[snezinka])

        # zapisemo, kdaj se je nazadnje ponovila trenutna snezika
        skatla[snezinka] = zap_st_snezinke
        # tukaj moremo potem vzeti najdaljše zaporedje - to je lahko ali trenutno zaporedje ali prejšnje najdaljše
        najdaljse_zaporedje = max(trenutno_nepretrgano_zaporedje, najdaljse_zaporedje)

    print(najdaljse_zaporedje)

