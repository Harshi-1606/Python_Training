'''wap to create student class and print object reference'''

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# class Student():
#     name = "Harshi"
#     email = "h@email.com"
#     print(name, email)
# s1 = Student()
# print(s1)

# class Student():
#     name = "Harshi"
#     email = "h@email.com"
#     def display(abc):
#         print(abc.name, abc.email)
# s1 = Student()
# s1.display()
# print(s1)

'''Take 2 variables as first name and last name and display the values with the help of function'''

# class Name():
#     def __init__(self,first,last):
#         self.first_name = first
#         self.last_name = last
#     def display(self):
#         print(self.first_name, self.last_name)
# # f_na = input("Enter first name: ")
# # l_na = input("Enter last name: ")
# # N1 = Name(f_na,l_na)
# # N2 = Name(f_na,l_na)
# N1 = Name("abc", "xyz")
# N2 = Name("def", "uvw")
# N1.display()
# N2.display()
# print(N1)

'''Implement multi-user environment with the help of constructor and display values'''

class Name():
    def __init__(self,first,last):
        self.first_name = first
        self.last_name = last
    def __str__(self):
        return self.first_name + self.last_name
    def display(self):
        print(self.first_name, self.last_name)
for i in range(2):
    f_na = input("Enter first name: ")
    l_na = input("Enter last name: ")
N1 = Name(f_na,l_na)
N2 = Name(f_na,l_na)
N3 = Name("abc", "xyz")
# N4 = Name()
N1.display()
N2.display()
N3.display()
# print(N1)



'''Simulate predefined str method to return a string which is containing lname and fname '''







