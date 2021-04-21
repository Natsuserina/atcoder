INF = 1_000_000_000_000_000_000

N, M = map(int, input().split())

dist = []
for i in range(N):
    dist.append([])
    for j in range(N):
        dist[i].append(INF)

for _ in range(M):
    u, v, c = map(int, input().split())
    dist[u][v] = c

for i in range(N):
    dist[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = 0

for i in range(N):
    for j in range(N):
        ans += dist[i][j]

print(ans)
