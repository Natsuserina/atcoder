import heapq

N, M = map(int, input().split())
G = []
for i in range(N):
    G.append([])
for i in range(M):
    u, v, c = map(int, input().split())
    G[u].append((c, v))
    G[v].append((c, u))

dist = [-1]*N
dist[0] = 0

done = [False]*N

Q = []

heapq.heappush(Q, (0, 0))

while len(Q) > 0:

    d, i = heapq.heappop(Q)

    if done[i]:
        continue
    
    done[i] = True

    for (c, j) in G[i]:
        if dist[j] == -1 or dist[j] > dist[i] + c:
            dist[j] = dist[i] + c
            heapq.heappush(Q, (dist[j], j))

print(dist[N-1])

