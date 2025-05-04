def example_1():
    my_list = [10, [99, 109, 1], "hello"]
    print("===List Value====")
    print(my_list[0])
    print(my_list[1])
    print(my_list[2])


def example_2():
    my_dict = {"first_key": "first_value", 2: [34, 1000], (1,2,3): 4324}
    print(my_dict["first_key"])
    print(my_dict[2])
    print(my_dict[(1, 2, 3)])


def example_3():
    dict_1 = {"first_key": "first_value", "second_key": "second_value", "third_key":"third_value"}
    print(type(dict_1))
    print(dict_1)


def example_4():
    dict_2 = dict([["first_key", "first_value"],["second_key", "second_value"]])
    print(type(dict_2))
    print(dict_2)


def example_5():
    dict_3 = dict.fromkeys(["key_1", "key_2", "key_3"], "value")
    print(type(dict_3))
    print(dict_3)