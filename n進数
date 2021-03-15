az = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def ex_10_n(x, n):
    if (int(x/n)):
        return ex_10_n(int(x/n), n) + az[x%n]
    return az[x%n]

N = int(input())
ans = ex_10_n(N, 36)
print(ans)
