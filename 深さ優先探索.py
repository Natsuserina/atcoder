import sys
sys.setrecursionlimit(1000000)

visited = []
for i in range(N):
    visited.append(False)

def dfs(i):
    visited[i] = True
    for j in E[i]:
        if not visited[j]:
            dfs(j)

dfs(i)

#2次元グリッド
def dfs(i, j):
    visited[i][j] = True
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        i2 = i+di
        j2 = j+dj
        if not (0 <= i2 < H and 0 <= j2 < W):
            continue
        if not A[i2][j2]:
            continue
        if not visited[i2][j2]:
            dfs(i2, j2)
