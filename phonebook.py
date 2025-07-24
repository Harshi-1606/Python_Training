import time
def main():
    phonebook = {}

    while True:
        print("\nPhonebook Application")
        print("1. Add New Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. List All Contacts")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter contact name: ")
            if name in phonebook:
                print("Contact already exists!")
                time.sleep(3)
            else:
                phone = input("Enter phone number: ")
                phonebook[name] = phone
                print("Contact added.")
                time.sleep(3)

        elif choice == "2":
            name = input("Enter contact name to search: ")
            if name in phonebook:
                print(f"{name}: {phonebook[name]}")
                time.sleep(3)
            else:
                print("Contact not found.")
                time.sleep(3)

        elif choice == "3":
            name = input("Enter contact name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print("Contact deleted.")
                time.sleep(3)
            else:
                print("Contact not found.")
                time.sleep(3)

        elif choice == "4":
            if not phonebook:
                print("Phonebook is empty.")
                time.sleep(3)
            else:
                print("All Contacts:")
                for name, phone in phonebook.items():
                    print(f"{name}: {phone}")
                    time.sleep(3)

        elif choice == "5":
            print("Exiting Phonebook. Goodbye!")
            time.sleep(3)
            break

        else:
            print("Invalid option. Please choose 1-5.")
            

if __name__ == "__main__":
    main()
