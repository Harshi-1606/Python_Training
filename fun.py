# def function_name(name= 'abc', age = 0):
#     print(name)
#     print(age)
#
# function_name(age = 1, name =3)
# function_name(7,4)
# function_name()
#
# # Multiple arguments when unknown to dev
# def function_name2(*parameter):
#     print(parameter)
#
# function_name2("harshith", 20)


# def add1(a,b):
#     print(a+b)
#
# def add1(a = 0):
#     print(a)
#
# add1(2,3)

# wap to display max number among 3 given integer, use function to do the calculation
# Note: inputs are integer not a list

# def max_val(a: int,b: int,c: int):
#     if a>b and a>c:
#         return a
#     elif b>c:
#         return b
#     else:
#         return c
#
# print(max_val(1,2,3))
#
# # Wap to check and return true if a user given number is power of 2
#
# def is_power_of_two(n):
#     if n <= 0:
#         return False
#     return (n & (n - 1)) == 0  # Bitwise method
#
# # Take input from the user
# num = int(input("Enter a number: "))
#
# # Check and display result
# if is_power_of_two(num):
#     print("True - It is a power of 2")
# else:
#     print("False - It is NOT a power of 2")
#
# def my_function():
#     pass    # Use pass to run empty function
#
# my_function()




# Wap to check given number is perfect square root or not


#Wap to print even numbers present in a range of 1 - 10 without using looping control statements


# def even(n=1):
#     if n <=5:
#         print(n*2)
#         even(n+1)
# even()

# Wap to display list of numbers present in a range of 1 -> 100 which are completely divisible by 3 & 5

# def divisible(n=1):
#     if n > 100:
#         return
#     if n % 3 == 0 or n % 5 == 0:
#         print(n)
#     divisible(n+1)
# divisible()

#Factorial

def fact(n):
    if n < 1:
        return
    elif n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))


#Tower of hanoi
