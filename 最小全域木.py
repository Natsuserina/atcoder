import heapq

N, M = map(int, input().split())
G = [[] for i in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a-1].append((b-1, c))
    G[b-1].append((a-1, c))

marked = [False]*N
marked_count = 0
marked[0] = True
marked_count += 1

#次に選ぶ辺の候補を入れるヒープ
Q = []
for j, c in G[0]:
    heapq.heappush(Q, (c, j))

#最小全域木の重みの合計を保存する変数
sum = 0
#全ての頂点がマークされるまで繰り返す
while marked_count < N:
    #ヒープから最小の辺を取り出す
    #（辺の重み、選んだ時にマークする頂点）
    c, i = heapq.heappop(Q)
    if marked[i]:
        continue
    marked[i] = True
    marked_count += 1
    sum += c
    #新たにマークした頂点に隣接する辺を調べる
    for (j, c) in G[i]:
        if marked[j]:
            continue
        heapq.heappush(Q, (c, j))

print(sum)
