def dan_v_letu(datum):
    '''pove nam kateri dan v letu je dani datum'''
    meseci = {'JAN': 31,
          'FEB': 29,
          'MAR': 31,
          'APR': 30,
          'MAY': 31,
          'JUN': 30,
          'JUL': 31,
          'AUG': 31,
          'SEP': 30,
          'OCT': 31,
          'NOV': 30,
          'DEC': 31}
    tab_mesecev = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    vsota = 0
    for mesec in tab_mesecev:
        if datum[1] == mesec:
            break
        else:
            vsota += meseci[mesec]
    vsota += int(datum[0])
    return vsota
            

def kateriDanJe(st_dneva, prvi_dan):
    '''funkcija nam pove kateri dan v tednu je če ji podamo
       začtni dan v letu ter zaporedno stevilko dneva v letu'''
    dnevi = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    ostanek = st_dneva % 7
    iskani_dan = dnevi[(dnevi.index(prvi_dan) - 1 + ostanek) % 7]
    return iskani_dan

datum = input().split()
prvi_dan = input()
# ugotovimo kateri dan v letu za povrstjo je dani datum
st_dneva = dan_v_letu(datum)
# s pomočjo začetnega dneva v tednu določimo dan za dani datum
iskani_dan = kateriDanJe(st_dneva, prvi_dan)
# če je dan pred 29.februarjem, ne rabimo upoštevati prestopnega leta
if st_dneva < (31 + 30):
    if iskani_dan == 'FRI':
        print('TGIF')
    else:
        print(':(')
# če pa je za marcem, je dan lahko petek le, če je najdeni dan petek ali pa sobota!!
# v tem primeru dneva ne moremo natančno določiti (izpišemo 'not sure')
else:
    if iskani_dan == 'FRI' or iskani_dan == 'SAT':
        print('not sure')
    else:
        print(':(')


