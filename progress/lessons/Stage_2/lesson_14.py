def example_1():
    sequence_1 = range(5)
    print(sequence_1, type(sequence_1))

    for iterator in sequence_1:
        print(iterator)

def example_2():
    new_list = list(range(5))
    print(new_list, type(new_list))

def example_3():
    for i in range(7, 10):
        print(i)

def example_4():
    for i in range(0, 11, 2):
        print(i)

def example_5():
    for i in range(5):
        print(i)
        for j in range(10,15):
            print(j)

def example_6():
    for i in range(2, 10):
        print(f"=={i}==")
        for j in range(2, 10):
            print(f"{i}*{j}={i*j}")