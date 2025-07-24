# d = {
#     'name': 'abc',
#     'age': 20
# }
# print(d)
#
# for i in d:
#     print(i)
#
# for i, h in zip(d.keys(), d.values()):
#     print(i,h)

#Wap to declare dictionary with 3 key and value pair and print dictionary

# d1 = {
#     'name': 'abc', 'age': 20, 'place': 'mangalore',
#
#
# }

'''Wap to display the menu of the restaurant with the key and value pair where keys are items available in the 
restaurant and values are prices of the respective items, take the order from the end user and generate
invoice and display
'''
# menu = {
#     'item1': 25,
#     'item2': 10,
#     'item3': 20,
#     'item4': 30,
# }
#
# # print("Item", "Price")
# # for k, v in menu.items():
# #     print(k, v)
#
# order ={}
#
# while True:
#     choice = input("Which item would you like to order? ")
#     if choice in menu:

# Restaurant Menu (key: item name, value: price)
menu = {
    "Burger": 100,
    "Pizza": 250,
    "Sandwich": 80,
    "Pasta": 120,
    "Coke": 40
}

# Display the Menu
print("Welcome to Python Café!")
print("\nMenu:")
print("-" * 30)
for item, price in menu.items():
    print(f"{item:<10} : ₹{price}")
print("-" * 30)

# Take Order
order = {}
while True:
    choice = input("\nEnter item to order (or type 'done' to finish): ").title()

    if choice == 'Done':
        break
    elif choice in menu:
        qty = int(input(f"Enter quantity for {choice}: "))
        if choice in order:
            order[choice] += qty
        else:
            order[choice] = qty
    else:
        print("Item not available. Please choose from the menu.")

# Generate and Display Invoice
print("\nInvoice:")
print("-" * 40)
total = 0
for item, qty in order.items():
    price = menu[item]
    subtotal = price * qty
    total += subtotal
    print(f"{item:<10} x {qty:<3} = ₹{subtotal}")
print("-" * 40)
print(f"{'Total':<15}     ₹{total}")
print("Thank you for visiting Python Café!")


'''
assignment
WAP to maintain phonebook with the name and phone number, declare 4 methods such as add new contact, 
remove existing contact, search contact with the help of contact name and display, give 4 option to end user
'''

'''Wap to check whether user entered number is circular prime or not
constraint: only 2 digit number'''