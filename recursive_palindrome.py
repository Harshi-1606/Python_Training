
# def is_palindrome(s, start=0, end=None):
#     if end is None:
#         s = s.lower()
#         end = len(s) - 1
#     if start >= end:
#         return True
#     if s[start] != s[end]:
#         return False
#     return is_palindrome(s, start + 1, end - 1)
#
# print(is_palindrome("Racecar"))  # True
# print(is_palindrome("Python"))   # False

# def fibonacci(n):
#     if n < 0:
#         return "Not defined"
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# s = int(input())
# print(fibonacci(s))


# Wap to display list of fibonacci numbers
def fibonacci(n):
    a , b = 0, 1
    if n < 0:
        return "Not defined"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return a , b = b , a + b


# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=' ')
#         a, b = b, a + b
#
# # Example: Display first 10 Fibonacci numbers
# fibonacci(10)

# wap to display armstrong numbers in a given range


memo = ()
def stepPerms(n)

'''Wap to demonstrate set methods which should contain add, remove, discard 
Initial set: 1,11,17,true,21,1,true
add 7 to the set
remove 1 from the set
discard true

'''