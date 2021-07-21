from collections import deque

N, M = map(int, input().split())
G = []
for i in range(N):
    G.append([])
Dim = [0]*N
for i in range(M):
    u, v = map(int, input().split())
    G[u-1].append(v-1)
    Dim[v-1] += 1

Q = deque()
for i in range(N):
    if Dim[i] == 0:
        Q.append(i)

while len(Q) > 0:
    i = Q.popleft()
    for j in G[i]:
        Dim[j] -= 1
        if Dim[j] == 0:
            Q.append(j)

for i in range(N):
    if Dim[i] > 0:
        print('Yes')
        exit()
print('No')
