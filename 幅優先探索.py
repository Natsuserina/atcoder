from collections import deque
#頂点数N、辺情報E、始点sは与えられている
N, M = map(int(input().split()))
G = [[] for i in range(N)]
for i in range(M):
    s, t = map(int, input().split())
    G[s-1].append(t-1)

Q = deque()
dist = [-1]*N
Q.append(s)
dist[s] = 0

#キューから取り出しながら探索する
while len(Q) > 0:
    i = Q.popleft()
    for j in G[i]:
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            Q.append(j)
            
