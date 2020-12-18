#PASSWORD HACKING
st_vpisov = int(input())
moznosti = [] #naredimo tabelo, da lahko dostopamo do indeksov vnesenih podatkov
for _ in range(st_vpisov):
    tmp_tabela = input().split(' ') #vnesemo gesla in verjetnosti
    moznosti.append(float(tmp_tabela[1])) #v tabelo dodajamo (samo) verjetnosti

moznosti.sort(reverse = True) #z namenom, da razvrsti od največjega do najmanjšega
st_poiskusov = 0
i = 1
while i <= st_vpisov:
    st_poiskusov += moznosti[i - 1] * i
    #mnozimo po optimalnem vrtnem redu in prištevamo prejšnje poiskuse
    #prvega mnozimo z 1, drugega z 2...itd
    i = i + 1

print(st_poiskusov)




