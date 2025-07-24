# a = int(input("Enter number a "))
# b = int(input("Enter number b "))
#
# print(a + b)
# print(a - b)
# print(a * b)


#n = int(input())
# if n % 2 != 0:

# n = int(input())
# for i in range (0, n):
#     print(i*i)

# you = 5
# date = 10
# if you >= 8 or date >= 8:
#     print("2")
# elif you <= 2 or date <= 2:
#     print("0")
# else:
#     print("1")

# 1. write a program to print sum of digits present in a given number

# n = 1234
# sum = 0
# while n!=0:
#     rem = n % 10
#     if rem % 2 == 0:
#         sum += rem
#     n = n // 10
#
# print(sum)

# wap to display list of prime number present in the range 1 - 10

# primes = []
# for num in range(2, 11):
#     for i in range (2, int(num**0.5) +1):
#         if num % i == 0:
#             break
#         else:
#             primes.append(num)
# print(primes)

n = 10
for i in range(1, n+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)

# isPrime = True
# def primeno(num):
#     for i in range (2, n-1):







