def isPrime(n):
    #vrne ce je prastevilo ali ne
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    i = 1
    while (i * i <= n): 
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 1
    return True
    
def modInversePrime(a, m): 
    #vrne "power" od a, m-2 in m ali pa impossible ce gcd ni 1  
    g = gcd(a, m) 
    if (g != 1):
        return "IMPOSSIBLE"
    else:
        #Če je skupni delitelj a in m samo 1, 
        #potem je mod inverz  a^(m-2) mode m 
        return power(a, m - 2, m)
      
 
def power(x, y, m):
    # izračuna x**y pod modulom m
    if (y == 0):
        return 1
    p = power(x, y // 2, m) % m 
    p = (p * p) % m
    if (y % 2 == 0):
        return p  
    else:
        return ((x * p) % m)
  
# gcd vrne največji skupni delitelj a in b
def gcd(a, b): 
    if (a == 0):
        return b 
    return gcd(b % a, a)


def modInverse(a, m):
    # vrne mod inverz števil a in m
    try:
        m0 = m 
        y = 0
        x = 1
        if (m == 1):
            return a + 1
        while (a > 1):
            #q je količnik a in m 
            q = a // m 
            t = m 
            #Zdaj je m ostanek pri a // m, isto kot euclid
            m = a % m 
            a = t 
            t = y 
            #končno prepišemo x and y 
            y = x - q * y 
            x = t 
        #x naredimo pozitiven 
        if (x < 0): 
            x = x + m0
        return x
    except:
        return 'IMPOSSIBLE'

koliko = int(input())
for i in range(koliko):
    vr = input().split()
    k = int(vr[0])
    c = int(vr[1])
    if isPrime(k):
        x = modInversePrime(c, k)
    else:    
        x = modInverse(c, k)
    print(x)