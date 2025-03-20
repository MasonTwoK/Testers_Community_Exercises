list_1 = [1, 2, 3, 1, 777]
list_2 = [1, 777, 999]

def example_1():
    print(dir([1, 2, 3]))

def example_2(list_a, list_b):
    list_a.append(555)
    print(list_a)

    list_a.append(list_b)
    print(list_a)

def example_3(list_a, list_b):
    list_a.extend(list_b)
    print(list_a)

def example_4_list_insert(list_of_something, index, object_for_list):
    list_of_something.insert(index, object_for_list)
    print(list_of_something)

def example_5_list_count(list_of_something, value):
    print(list_of_something.count(value))

def example_6_list_index(list_of_something, value):
    # function returns inedex of first entered value starting from left side
    print(list_of_something.index(value))

def example_7_list_reverse(list_of_something):
    print(f"Current list: {list_of_something}")
    list_of_something.reverse()
    print(f"List after reverse: {list_of_something}")

def example_8_list_pop(list_of_something, index_of_element):
    print(f"Base list: {list_of_something}")
    popped_element_of_list = list_of_something.pop(index_of_element)
    print(f"List after element {index_of_element} pop: {list_of_something}")
    print(f"Popped element: {popped_element_of_list}")

def example_9_list_remove(list_of_something, value_of_element):
    print(f"Base list: {list_of_something}")
    print(f"List after element {value_of_element} remove: {list_of_something}")

def example_10_list_copy(list_of_something):
    new_list = list_of_something.copy()

    print(f"Base list: {list_of_something}")
    print(f"Base list id: {id(list_of_something)}")

    print(f"Content of new list: {new_list}")
    print(f"New list id: {id(new_list)}")

def example_11_list_sort(list_of_something, reverse_order=False):
    print(f"Base list: {list_of_something}")
    list_of_something.sort(reverse=reverse_order)
    print(f"Sorted list: {list_of_something}")

grocery_list = ['banana', 'strawberry', 'peach', 'apple', 'mango']

def example_12_list_clear(list_of_something):
    print(f"Base list: {list_of_something}")
    list_of_something.clear()
    print(f"List after clear: {list_of_something}")

# print(list_of_nums.index(2))  # Returns 1 (value under index 2)
# print(list_of_nums.copy())  # Returns same list
# print(list_of_nums.pop(1))  # Returns 2 (popped value)
#
# result = list_of_nums.sort()
# print(result)  # Returns None
#
# print(list_of_nums.append(4))  # Returns None
# print(list_of_nums.extend([4]))  # Returns None
# print(list_of_nums.reverse())  # Returns None
# print(list_of_nums.clear())  # Returns None