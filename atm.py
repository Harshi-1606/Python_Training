''' WAP to implement simple atm application and print the following options and perform
user selected option
1. Deposit
2. Withdrawal
3. Balance check
4. Pin change'''
import time

pin = 8285
amount = 1000


def deposit():
    global amount
    print("Enter pin")
    d_pin = int(input())
    if d_pin == pin:
        print(" Place the cash in the tray")
        print("Enter amount ")
        am = int(input())
        amount += am
        time.sleep(3)
        print(f"Amount {am} deposited successfully")
    else:
        print("Invalid pin")


def withdraw():
    global amount
    print("Enter pin")
    w_pin = int(input())
    if w_pin == pin:
        print("Enter amount to withdraw")
        amt = int(input())
        if amt <= 0:
            print("Amount cannot be less than zero")
        else:
            time.sleep(2)
            print("Amount withdrawn")
            amount -= amt
            time.sleep(2)
            print(f"Remaining balance {amount}")
    else:
        print("Invalid pin")


def balance():
    print(f"Balance amount: {amount}")


def pin_change():
    global pin
    print("Enter new pin ")
    us_pin = int(input())
    pin = us_pin
    print("Pin changed successfully")


print("Welcome to cashless atm")
# print("Insert Debit Card")
print("Press any key to continue")
s = input()
ch = 0
if s.isalnum():
    print("Enter pin")
    u_pin = int(input())
    if u_pin == pin:
        while True:
            time.sleep(2)
            print("Select Option")
            print("1. Deposit \n2. Withdrawal \n3. Balance check \n4. Pin change \n5. Exit")
            ch = int(input())
            if ch == 1:
                deposit()
            elif ch == 2:
                withdraw()
            elif ch == 3:
                balance()
            elif ch == 4:
                pin_change()
            elif ch == 5:
                break
            else:
                print("Invalid input")
                time.sleep(2)


    else:
        print("Pin doesn't match")
