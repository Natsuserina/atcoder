import sys
sys.setrecursionlimit(1000000)

N = int(input())

memo = [0]*(N+1)

def fib(i):
    if i <= 1:
        return i
    if memo[i] != 0:
        return memo[i]
    memo[i] = fib(i-1) + fib(i-2)
    return memo[i]

print(fib(N))
