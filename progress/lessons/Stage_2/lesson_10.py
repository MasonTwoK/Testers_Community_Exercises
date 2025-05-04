
my_tuple_1 = (1, 2, 3)
print(type(my_tuple_1), my_tuple_1)

my_tuple_2 = 1, 2, 3
print(type(my_tuple_2), my_tuple_2)

# conveting list to tuple
my_tuple_3 = tuple([1, 2, 3])
print(type(my_tuple_3), my_tuple_3)

print(my_tuple_3[0], my_tuple_3[2])

print(len(my_tuple_3))

print(1 in my_tuple_3)
print(2 not in my_tuple_3)

my_tuple_4 = 4, 5, 6
print(my_tuple_3 + my_tuple_4)
print(my_tuple_4 + my_tuple_3)

for iterator in my_tuple_1:
    print(iterator)

print(max(my_tuple_1))
print(min(my_tuple_1))

my_tuple_5 = 1,2,3,4,5,1
print(my_tuple_5.index(1))
print(my_tuple_5.count(1))