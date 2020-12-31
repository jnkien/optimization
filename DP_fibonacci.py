def fib_naive(n):
    if n<=2:
        f = 1
    else:
        f = fib_naive(n-2) + fib_naive(n-1)
    return f

# memoized version
memo = {}
def fib_mem(n):
    if n in memo.keys():
        return memo[n]
    if n<=2:
        f = 1
    else:
        f = fib_mem(n-2) + fib_mem(n-1)
    memo[n] = f
    return f

# bottom-up version
def fib_botup(n):
    memo = {}
    for k in range(1, n+1):
        if k<=2:
            f = 1
        else:
            f = memo[k-2] + memo[k-1]
        memo[k] = f
    return memo[n]

# print(fib_naive(35) == 9227465) #18454933 function calls (5 primitive calls) in 5.105 seconds
# print(fib_mem(35) == 9227465) #138 function calls (72 primitive calls) in 0.000 seconds
print(fib_botup(35) == 9227465) #5 function calls in 0.000 seconds
