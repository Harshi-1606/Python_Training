'''write a program to simulate library management system with the help of class & object, basic data type,
dictionary. Design & implement library management, those systems should allow librarians & users to manage
books & respective records
a) Create a sub-function as add_book, remove_book, search_book & display list of books present in the library'''

class Library:
    def __init__(self):
        self.books = {}
    def add_book(self, bookID, bookName, Author):
        if bookID in self.books:
            print("Book already exists")
        else:
            self.books[bookID] = {"name": bookName, "author":Author}
            print("New book added")

    def remove_book(self, bookID):
        if bookID in self.books:
            del self.books[bookID]
            print("Book removed")
        else:
            print("Book not found")

    def search_book(self, bookID):
        if bookID in self.books:
            print("Book found")
            print(self.books[bookID])
            print(self.books[bookID]["name"])
            print(self.books[bookID]["author"])
        else:
            print("Book not found")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Books in library:")
            for bookID, book in self.books.items():
                print("ID:", bookID, "| Name:", book["name"], "| Author:", book["author"])


def main():
    library = Library()

    while True:
        print("\nChoose an option:")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search a Book")
        print("4. Show All Books")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            try:
                book_id = int(input("Enter book ID (number): "))
                book_name = input("Enter book name: ")
                author_name = input("Enter author name: ")
                library.add_book(book_id, book_name, author_name)
            except:
                print("Invalid input. Book ID should be a number.")

        elif choice == "2":
            try:
                book_id = int(input("Enter book ID to remove: "))
                library.remove_book(book_id)
            except:
                print("Invalid input. Book ID should be a number.")

        elif choice == "3":
            try:
                book_id = int(input("Enter book ID to search: "))
                library.search_book(book_id)
            except:
                print("Invalid input. Book ID should be a number.")

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Please enter a valid choice from 1 to 5.")


if __name__ == "__main__":
    main()


''' Wap to manage users of library by creating userid, username, user_contact as data members where
 add_user, search_user, List_of_users are function members based on end user details and requirements create
 user management system
 Note: to store the data use a dictionary called as user'''

class User:
    def __init__(self, user_id, username, contact):
        self.user_id = user_id
        self.username = username
        self.contact = contact

class UserManagement(User):
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user.user_id in self.users:
            print("User ID already exists")
        else:
            # extract data from User object and store in dictionary
            self.users[user.user_id] = {
                "username": user.username,
                "contact": user.contact
            }
            print("User added")

    def search_user(self, user_id):
        if user_id in self.users:
            user = self.users[user_id]
            print(f"Found User - ID: {user_id}, Name: {user['username']}, Contact: {user['contact']}")
        else:
            print("User not found")

    def list_users(self):
        if not self.users:
            print("No users found")
        else:
            for uid, info in self.users.items():
                print(f"ID: {uid}, Name: {info['username']}, Contact: {info['contact']}")

def main():
    um = UserManagement()
    n = int(input("How many users to add? "))
    for _ in range(n):
        user_id = input("Enter user ID: ")
        username = input("Enter username: ")
        contact = input("Enter contact: ")
        user = User(user_id, username, contact)  # create User instance
        um.add_user(user)  # add user object to UserManagement

    while True:
        print("\n1. Add User\n2. Search User\n3. List Users\n4. Exit")
        choice = input("Choice: ")
        if choice == "1":
            user_id = input("Enter user ID: ")
            username = input("Enter username: ")
            contact = input("Enter contact: ")
            user = User(user_id, username, contact)
            um.add_user(user)
        elif choice == "2":
            user_id = input("Enter user ID to search: ")
            um.search_user(user_id)
        elif choice == "3":
            um.list_users()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
