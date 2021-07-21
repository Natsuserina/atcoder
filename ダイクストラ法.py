import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
G = []
for i in range(N):
    G.append([])
for i in range(M):
    u, v, t = map(int, input().split())
    G[u-1].append((t, v-1))
    G[v-1].append((t, u-1))

time = [-1]*N
time[0] = 0
done = [False]*N
Q = []
heapq.heappush(Q, (0, 0))

while len(Q) > 0:

    d, i = heapq.heappop(Q)
    if done[i]:
        continue
    done[i] = True

    for (t, j) in G[i]:
        if time[j] == -1 or time[j] > time[i] + t:
            time[j] = time[i] + t
            heapq.heappush(Q, (time[j], j))

print(time[N-1])
