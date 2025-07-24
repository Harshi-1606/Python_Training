''' wap a program to find fibonacci series of nth term using dynamic programming'''


'''1)wap to display factorial of n 
calculate factorial of n using recursion + memoization
'''

#1
def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n = 5
print("Factorial (iterative) of", n, "is", factorial_iterative(n))

def factorial_recursive_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = 1
    else:
        memo[n] = n * factorial_recursive_memo(n-1, memo)
    return memo[n]

n = 5
print("Factorial (recursive + memoization) of", n, "is", factorial_recursive_memo(n))

'''
2) climbing stair problem
GOal: count the ways to reach the top of stairs by taking 1 or 2 steps'''


def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b

stairs = 5
print("Ways to climb", stairs, "stairs is", climb_stairs(stairs))


def climb_stairs_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        memo[n] = n
    else:
        memo[n] = climb_stairs_memo(n-1, memo) + climb_stairs_memo(n-2, memo)
    return memo[n]

stairs = 5
print("Ways to climb", stairs, "stairs (recursive + memoization):", climb_stairs_memo(stairs))
