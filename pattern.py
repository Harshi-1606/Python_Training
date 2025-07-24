# n = 5
# c = 'H'
# for i in range(n):
#     print((c * i).rjust(n) + c + (c*i).ljust(n))
#     # print(c*i)

# for i in range(4, 0, -1):
#     print(str(i) * i)

c = 'H'
n = 5
#Triangle
for i in range (n-1):
    print((c*i).rjust(n-1) + c + (c*i).ljust(n-1))
# Vertical
for i in range (n):
    print((c*n).center(5*2)+ (c*n).center(5*6))
# Horizontal
for  i in range(3):
    print((c*6).center(5*2) + (c*9).ljust(5*2) + (c*5).center(5*2))
# Vertical
for i in range (n):
    print((c*n).center(5*2)+ (c*n).center(5*6))
# Reversed Triangle
for i in range(n):
    print(((c * (n - i - 1)).rjust(n) + c + (c*(n - i - 1)).ljust(n)).rjust(n * 6))