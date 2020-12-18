import string

niz = input()
prazen = ''
for element in niz:
    if element in string.ascii_uppercase:
        prazen += element
        
print(prazen)