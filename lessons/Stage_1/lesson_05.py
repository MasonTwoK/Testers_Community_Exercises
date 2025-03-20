from os import remove


def example_1():
    list_empty = []
    print(list_empty, type(list_empty))

def example_2():
    list_a = [12, "hello", 34.0, True, [23, 789]]

    print(list_a[0])
    print(list_a[2])
    print(list_a[4][1])

def example_3():
    list_a = [12, "hello", 34.0, True, [23, 789]]

    print(list_a[0])
    list_a[0] = 13
    print(list_a[0])

def example_4():
    list_items_str = input("Type a list of products: ")
    list_items = list_items_str.split(" ")
    print(list_items, type(list_items))

    return list_items

def example_5(grocery_list):
    to_delete_item = input("Insert item you want to remove: ")
    grocery_list.remove(to_delete_item)

    print(grocery_list)

def example_6(grocery_list):
    print("Last list item remover called")
    grocery_list.pop()
    print(grocery_list)

def example_7(grocery_list):
    del_num = int(input("Insert number which is need to be deleted: "))
    grocery_list.pop(del_num-1)
    print(grocery_list)


