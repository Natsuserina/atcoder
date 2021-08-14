N = int(input())

#pair[i]:頂点iの根。par[i]==iの時、自分がグループの根。
pair = [i for i in range(N)]
#size[i]:頂点iを部分木の根とみなしたときのその木の大きさ。
size = [1]*N

def find(x):
    #根に到達したら、その頂点を返す
    if pair[x] == x:
        return x
    else:
        #経路圧縮
        pair[x] = find(pair[x])
        return pair[x]

def union(x, y):
    rx, ry = find(x), find(y)
    #同じグループなら何もしない
    if rx == ry:
        return
    #どちらの部分木が大きいか判断して、大きいほうの木に小さい木を併合する
    if size[rx] < size[ry]:
        size[ry] += size[rx]
        pair[rx] = ry
    else:
        size[rx] += size[ry]
        pair[ry] = rx

def same(x, y):
    return find(x) == find(y)
