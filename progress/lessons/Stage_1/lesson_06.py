
def example_1():
    for i in [1,2,3]:
        print(i)
        input()

    print("new line")

def example_2():
    for i in "Hello Python":
        print(i)

def example_3():
    nums_list = [-99, 100, 207, -3, 15]

    for i in nums_list:
        if i > 0:
            print(i / 4)
        else:
            print(i + 20)
