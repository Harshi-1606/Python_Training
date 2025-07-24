# import random
#
# number = random.randint(1,10)
# while True:
#     guess_number = int(input("Guess a number between 1 and 10: "))
#     if guess_number == number:
#         print("Congratulations, you guessed it!")
#         break
#     elif number - guess_number <= 2:
#         print("Cold.")
#     elif number - guess_number >= 2:
#         print("Hot")


# print("\U0001F525")

'''wap to display count of given number in a a list
list= 7,49,7,11,6,41,7,1,101'''

numbers = [7, 49, 7, 11, 6, 41, 7, 1, 101]

target = int(input("Enter the number to count: "))
count = numbers.count(target)

print(f"The number {target} appears {count} time(s) in the list.")

