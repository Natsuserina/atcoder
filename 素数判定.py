def divisor(n): 
    i = 2
    table = [1, n]
    while i * i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

N = int(input())
print(divisor(N))
