def divisor(n): 
    i = 2
    while i * i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

N = int(input())
print(divisor(N))
