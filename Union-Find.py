N, M, K = map(int,input().split())

#par[i]:頂点iの根。par[i]==iの時、自分がグループの根。
par = [i for i in range(N)]
#sz[i]:頂点iを部分木の根とみなしたときのその木の大きさ。
sz = [1]*N
ans = [0]*N

def find(x):
    #根に到達したら、その頂点を返す
    if par[x] == x:
        return x
    else:
        #経路圧縮
        par[x] = find(par[x])
        return par[x]

def union(x, y):
    rx, ry = find(x), find(y)
    #同じグループなら何もしない
    if rx == ry:
        return
    #どちらの部分木が大きいか判断して、大きいほうの木に小さい木を併合する
    if sz[rx] < sz[ry]:
        sz[ry] += sz[rx]
        par[rx] = ry
    else:
        sz[rx] += sz[ry]
        par[ry] = rx

def same(x, y):
    return find(x) == find(y)

for _ in range(M):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    #友達関係は-1する
    ans[a] -= 1
    ans[b] -= 1
    union(a, b)

for _ in range(K):
    c,d = map(int,input().split())
    c -= 1
    d -= 1
    if same(c, d):
        #同じグループに所属しているブロック関係は-1する
        ans[c] -= 1
        ans[d] -= 1

for i in range(N):
    ans[i] += sz[find(i)] - 1
    print(ans[i], end=' ')
