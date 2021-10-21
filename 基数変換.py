#n == 0のとき気を付けて！！！！！！！！！！！！！
#n: str(), b: int(), return str()
def b_to_ten(n, b):
    l = len(n)
    base_ten = 0
    for i in range(l-1, -1, -1):
        base_ten += int(n[i])*b**(l-1-i)
    return str(base_ten)

#n: str(), b: int(), return str()
def ten_to_b(n, b):
    n = int(n)
    base_b = ''
    while n:
        base_b += str(n % b)
        n //= b
    base_b = base_b[::-1]
    return base_b
