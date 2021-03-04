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

