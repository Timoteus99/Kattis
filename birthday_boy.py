def kateriDan(dan):
    '''Kot argument dobi zaporedno st dneva v letu. Vrne pa datum v ustreznem zapisu MM-DD'''
    dneviVmesecu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mesec = 1 # zacnemo z ena, ker ni meseca 00
    for st in dneviVmesecu:
        if dan > st:
            dan = dan - st
            mesec += 1
        else: break
    
    # sedaj imamo st (1-31) v spremenljivki dan
    # in st (1-12) v spremenljivki mesec
        
    dan = str(dan)
    mesec = str(mesec)
    
    
    # dodati moramo se niclo pred enomestnim stevilom
    if len(str(dan)) == 1:
        dan = '0' + dan
    if len(str(mesec)) == 1:
        mesec = '0' + mesec
    
    return mesec + '-' + dan
        

def dolociDatum(datumi):
    '''Kot argument dobi tabelo datumov v obliki MM-DD. Vrne datum, ki ustrez pogojem naloge'''
    # st_dni predstavlja stevilko s katero se mesec zacne
    st_dni = {'01':0,
              '02':31,
              '03':59,
              '04':90,
              '05':120,
              '06':151,
              '07':181,
              '08':212,
              '09':243,
              '10':273,
              '11':304,
              '12':334}

    dan_v_mesecu = {'01':1,
                    '02':2,
                    '03':3,
                    '04':4,
                    '05':5,
                    '06':6,
                    '07':7,
                    '08':8,
                    '09':9,
                    '10':10,
                    '11':11,
                    '12':12,
                    '13':13,
                    '14':14,
                    '15':15,
                    '16':16,
                    '17':17,
                    '18':18,
                    '19':19,
                    '20':20,
                    '21':21,
                    '22':22,
                    '23':23,
                    '24':24,
                    '25':25,
                    '26':26,
                    '27':27,
                    '28':28,
                    '29':29,
                    '30':30,
                    '31':31}
    
    danes = st_dni['10'] + dan_v_mesecu['27']
    tab_dni = []
    for datum in datumi:
        dan = datum.split('-')[1]
        mesec = datum.split('-')[0]
        dan_v_letu = st_dni[mesec] + dan_v_mesecu[dan]
        tab_dni.append(dan_v_letu)
    
    tab_dni = sorted(tab_dni)
    # tu imamo ze tabelo dnevov ki so zapisa, kot zaporedna st datuma v letu
    
    
    tab_razlik = []
    naj_razlika = 0
    kje = 0
    while kje < len(tab_dni):
        
        if kje == len(tab_dni) - 1: # ker moramo pregledati tudi razliko med zadnjim in prvim datumom
            razlika = 365 - tab_dni[kje] + tab_dni[0]
            if razlika > naj_razlika:
                tab_razlik = [tab_dni[0]]
                naj_razlika = razlika
            elif razlika == naj_razlika:
                tab_razlik.append(tab_dni[0])
        
        else:
            elt = tab_dni[kje]
            razlika = tab_dni[kje + 1] - elt
            if razlika > naj_razlika:
                tab_razlik = [tab_dni[kje + 1]]
                naj_razlika = razlika
            elif razlika == naj_razlika:
                tab_razlik.append(tab_dni[kje + 1])
        kje += 1
    
    # v tab_razlik imamo torej shranjene datume (zaporedne st dni), ki so imeli za sabo najvecjo razliko
    # v tabeli so zato, ker moramo med njimi poiskati datum, ki je najbljizje 10-27
            
    if len(tab_razlik) == 1:
        iskani_dan = tab_razlik[0] - 1
    
    else:    
        najblizji_datum = 0
        min_razlika = 365
        for dan in tab_razlik:
            if dan - 1 > danes:
                razlika = dan - danes
                if razlika < min_razlika:
                    min_razlika = razlika
                    najblizji_datum = dan
            else:
                razlika = 365 - danes + dan
                if razlika < min_razlika:
                    min_razlika = razlika
                    najblizji_datum = dan
            
        iskani_dan = najblizji_datum - 1
        
    
    # iskani dan ne sme biti 00-00, ta namrec predstavlja datum 12-31  
    if iskani_dan == 0:
        iskani_dan = 365
        
    rez = kateriDan(iskani_dan)
    return rez

    
datumi = []
st_delavcev = int(input())
for delavec in range(0,st_delavcev):
    delavec = input()
    datumi.append(delavec.split()[-1])

print(dolociDatum(datumi))