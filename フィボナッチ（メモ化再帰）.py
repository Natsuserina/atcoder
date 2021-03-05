N = int(input())

def fib_memo(i):
    memo = [0]*(i+1)

    def fib(i):
        if i <= 1:
            return i
        if memo[i] != 0:
            return memo[i]
        memo[i] = fib(i-1) + fib(i-2)
        return memo[i]
    
    return fib(i)

print(fib_memo(N))