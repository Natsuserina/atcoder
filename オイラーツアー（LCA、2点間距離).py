import sys
sys.setrecursionlimit(1000000)

N, Q = map(int, input().split())
G = []
for i in range(N):
    G.append([])
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

visited = [False]*N
eular_tour = []
first_appear = [0]*N
dist = [-1]*N
p = 0
d = 0
def dfs(dep, v, vpre):
    global p
    global d
    if not visited[v]:
        first_appear[v] = p
    visited[v] = True
    eular_tour.append([dep, v])
    dist[v] = d
    p += 1
    d += 1

    for j in G[v]:
        if not visited[j]:
            dfs(dep+1, j, v)
    if dep > 0:
        eular_tour.append([dep-1, vpre])
        p += 1
        d -= 1

dfs(0, 0, 0)

for i in range(Q):
    c, d = map(int, input().split())
    pc = first_appear[c-1]
    pd = first_appear[d-1]
    if pc > pd:
        pc, pd = pd, pc
    SEC = eular_tour[pc:pd+1]
    dep = 10**9
    for sec in SEC:
        if dep >= sec[0]:
            lca = sec[1]
    D = dist[c-1] + dist[d-1] - 2*dist[lca]
    if D % 2 == 0:
        print('Town')
    else:
        print('Road')
