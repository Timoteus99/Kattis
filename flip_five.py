import copy

moves={(0,0),(-1,0),(0,1),(1,0),(0,-1)}





bounds={0,1,2}

pairs=[(i,j) for i in bounds for j in bounds]

nbrs=[set([i]) for i in xrange(9)]

for i in xrange(9):
    for j in xrange(i+1,9):
        ix,iy = pairs[i]
        jx,jy = pairs[j]
        if (jx-ix,jy-iy) in moves:
            nbrs[i].add(j)
            nbrs[j].add(i)



def toggle(state,i):
    for coord in nbrs[i]:
        state ^= (1<<coord)
    return state





def bfs(state):
    q=[(state,0)]
    visited = [False]*((1<<9))
    visited[state] = True
    while q:
        state , index = q.pop(0)
        if state==0:
            return index
        for i in xrange(9):
            newstate=toggle(state,i)
            if not visited[newstate]:
                q.append((newstate,index+1))
                visited[newstate] = True




    





p=int(raw_input())

for _ in xrange(p):
    grid=''.join([raw_input() for _ in xrange(3)])
    #print grid
    state = 0
    for c in reversed(grid):
        state<<=1
        state+= int(c=='*')
    print bfs(state)