# s = 'ABCDCDC'
# s1 = 'CDC'
# count = 0
# s3 = []
# for i in range(len(s) - len(s1) + 1):
#     if s[i:i+len(s1)] == s1:
#         count += 1
#         s3.append(s1)
# print(count, s3)

#Wap to check whether given number is armstrong number or not

# n = int(input("Enter number"))
# original_n = n
# d = 0
# while n!= 0:
#     rem = n%10
#     d += 1
#     n = n // 10
#
# print(original_n)
# print(d)

'''WAp to store student name, science marks, maths marks of 4 students to store name and marks use different list
1) Wap to print average marks based on entered name
'''

# name = ['abcd', 'efgh', 'ijkl', 'mnop']
# marks1 = [24,22,50,23]
# marks2 = [50,43,33,45]
#
# na = input("Enter name ")
# for i in range(0, len(name)):
#     y = name[i]
#     if y.lower() == na.lower():
#         print("name: ",na, "avg: ", marks1[i] + marks2[i] /2)

'''Wap to compare adjacent elements present in a list if 2 adjacent elements are same, move that 1
element to resultant list and unique element list which is containing all the uniquely entered value
present in a input  list'''

# a = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com" ]
#
# r = []
# for i in a:
#     if i not in r:
#         r.append(i)
#
# print(r)

'''Wap to find targeted element in a given list'''

a = ["a@gmail.com", "b@gmail.com", "a@gmail.com", "c@gmail.com", "g@gmail.com" ]
t = "g@gmail.com"
def ele(a,t):
    for i in range(len(a) -1):
        if t == list[i]:
            print(i)
    return -1
print(ele(a,t))