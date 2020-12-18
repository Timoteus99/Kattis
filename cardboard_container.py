prostornina = int(input()) # poiskati moramo visino, dolzino in pa širino lika pravokotnika ki ga potrebujemo

povrsina = 100000000 

for dolzina in range(int(prostornina ** (1/2)), 0, -1): # 2 od danih dolzin robov sta zagotovo manjša ali enak korenu od prostornine
    for sirina in range(1, int(prostornina ** (1/2)) + 1):
        if prostornina % (dolzina * sirina) == 0:
            visina = prostornina / (dolzina * sirina)
            nova_pov = 2*(dolzina * sirina) + 2 * (visina * sirina) + 2 * (dolzina * visina) # temu je enaka povrsina pravokotnika
            if nova_pov < povrsina: # poiskati moramo najmanjso mozno povrsino
                povrsina = nova_pov 

print(int(povrsina))
