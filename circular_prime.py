num = int(input("Enter a number to check if it is prime: "))

def reverse(cd):
    rev = 0
    while cd != 0:
        digit = cd % 10
        rev = rev * 10 + digit
        cd //= 10
    return rev
ab = reverse(num)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Check and display result
print(is_prime(num))
print(is_prime(ab))

if is_prime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is NOT a Prime Number.")

if is_prime(ab):
    print(f"{ab} is a Prime Number.")
else:
    print(f"{ab} is not a Prime Number.")






