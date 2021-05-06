N = int(input())
A = []
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

ALL = 1<<N

#すでに訪れた都市の集合n, 最後にいる都市がiであるときのコストの最小値
cost = []
for n in range(ALL):
    cost.append([10**100]*N)

cost[0][0] = 0

def bit(n, i):
    return (n & (1<<i)) > 0

#すでに訪れた都市の集合n、現在いる都市i、これから向かう都市j
for n in range(ALL):
    for i in range(N):
        for j in range(N):
            #もしjをすでに訪れているか、現在地が都市jならcontinue
            if bit(n, j) or i == j:
                continue
            
            cost[n|(1<<j)][j] = min(cost[n|(1<<j)][j], cost[n][i] + A[i][j])

print(cost[ALL-1][0])
