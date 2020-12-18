#ideja resevanja: vedno se znebimo polovice števil 
min_= 1
max_ = 1001 #ker je vključno z 1000
poiskus = 500 #vzamemo mediano, ker se tako znebimo največjega števila številk
print(str(poiskus), flush = True)

i = 0
while(True):
    x = input()
    if (x== "correct") or i >= 10:
        break
    #vedno za polovico zmanjšujemo intervale
    elif (x== "higher"):
        min_ = poiskus
    elif (x== "lower"):
        max_ = poiskus
    poiskus = int((max_  - min_) / 2 + min_) #izracunamo novo mediano
    i += 1
    print(poiskus, flush = True)
   
 