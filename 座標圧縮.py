#座標圧縮
import bisect

A = list(map(int, input().split()))
A_sort = sorted(A)
A_set = sorted(list(set(A_sort)))
#座標圧縮された配列
A_z = []

L = 0
value = 1
for s in A_set:
    R = bisect.bisect_right(A_sort, s)
    for i in range(L, R):
        A_z.append(value)
    value += 1
    L = R
