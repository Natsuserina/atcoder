def eratosthenes(n):
    prime = {i for i in range(2, n+1)}
    for i in range(2, n+1):
        if i in prime:
            for j in range(i*2, n+1, i):
                if j in prime:
                    prime.remove(j)
    return prime
