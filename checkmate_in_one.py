#Checkmate in one - kattis
#Link: https://open.kattis.com/problems/checkmateinone

def obstaja_mat():
    
    '''vrne 'Yes', če obstaja mat v 1
       in 'No', če ne obstaja mat v 1,
       v podani poziciji/problemu'''

    problem = []
    #vrstice zapnem v seznam
    for element in range(8):
        element = str(input())
        problem.append(element)

    indeks = 0 #vrstica indeks
    rook_indeks = 0 #indeks kje je trdnjava
    #for loop da najde pozicijo trdnjave
    for element in problem:
        if 'R' in element:
            rook_indeks = element.index('R')
    # preveri ce obstaja mat v 1 v vrsticah (levo in desno)
    for element in problem:
        if 'K.k' in element or 'k.K' in element:
            indeks = problem.index(element)
            if element[0] == 'k' or element[-1] == 'k':
                if 'R' not in element:
                    if (indeks == 0 and 'R' not in problem[1]) or indeks == 7 and 'R' not in problem[6]:
                        return 'Yes'
                    else:
                        if 'R' not in problem[indeks - 1] and 'R' not in problem[indeks + 1]:
                            return 'Yes'
    #preveri ce obstaja mat v 1 v stolpcih
    if ('k' in problem[0] and 'K' in problem[2]) or ('k' in problem[7] and 'K' in problem[5]):
        if 'k' in problem[0]: #zgornja stran
            if problem[0].index('k') == problem[2].index('K'):
                if (rook_indeks != problem[0].index('k') + 1) and (rook_indeks != problem[0].index('k') - 1):
                    if rook_indeks != problem[0].index('k'):
                        return 'Yes'
    
        if 'k' in problem[7]: #spodnja stran
            if problem[7].index('k') == problem[5].index('K'):
                if (rook_indeks != problem[7].index('k') + 1) and (rook_indeks != problem[7].index('k') - 1):
                    if rook_indeks != problem[7].index('k'):
                        return 'Yes'
    #preveri ce obstaja mat v 1 v levem zgornjem kotu
    if problem[0][0] == 'k':
        if problem[2][1] == 'K':
            if rook_indeks != 1:
                return 'Yes'
        if problem[1][2] == 'K' and 'R' not in problem[1]:
            return 'Yes'
    #preveri ce obstaja mat v 1 v desnem zgornjem kotu    
    if problem[0][-1] == 'k':
        if problem[2][-2] == 'K':
            if rook_indeks != 6:
                return 'Yes'
        if problem[1][-3] == 'K' and 'R' not in problem[1]:
            return 'Yes'
    #preveri ce obstaja mat v 1 v desnem spodnjem kotu    
    if problem[-1][-1] == 'k':
        if problem[-3][-2] == 'K':
            if rook_indeks != 6:
                return 'Yes'
        if problem[-2][-3] == 'K' and 'R' not in problem[-2]:
            return 'Yes'
    #preveri ce obstaja mat v 1 v levem spodnjem kotu    
    if problem[-1][0] == 'k':
        if problem[-3][1] == 'K':
            if rook_indeks != 1:
                return 'Yes'
        if problem[-2][2] == 'K' and 'R' not in problem[-2]:
            return 'Yes'
    #ce pride do sem, seveda mat v 1 ni mogoč, zato preprosto return 'No'    
    return 'No'

print(obstaja_mat())
