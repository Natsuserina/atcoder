import heapq

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    G[a-1].append((c, b-1))
    G[b-1].append((c, a-1))

def Dijkstra(s):
    dist = [-1]*N
    done = [False]*N
    Q = []
    heapq.heappush(Q, (0, s))
    dist[s] = 0
    while len(Q) > 0:
        d, i = heapq.heappop(Q)
        if done[i]:
            continue
        for c, j in G[i]:
            if dist[j] == -1 or dist[j] > dist[i] + c:
                dist[j] = dist[i] + c
                heapq.heappush(Q, (dist[j], j))
    return dist
