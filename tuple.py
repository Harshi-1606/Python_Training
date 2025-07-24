# t1 = (1,)
# t2 = 1,2,3
# t3 = ()
# print(type(t1))
# print(type(t2))

# print(len(t2))
# print(min(t2))
# print(max(t2))
# print(t2.count(2))
# print(t2.index(1))

#WAP to create, insert, delete and display tuple values where input is 1,4,6,9
# add element as 10, remove element 2, display tuple elements

tup =(1,4,6,9)

print("Tuple before modification: ", tup)
tup_list = list(tup)

tup_list.append(10)
tup_list.append(2)
print("Apppend 2", tup_list)
tup_list.remove(2)

tup = tuple(tup_list)

print("Tuple after modification: ", tup)

