from pyexpat.errors import messages


def example_1():
    list_a = []
    for iterator in range(1,11):
        list_a.append(iterator) # iterator [1,2,3,4,5,6,7,8,9,10]

    return list_a

def example_2(list_a):
    print(list_a[0])
    print(list_a[-1])
    print(list_a[:5])

def example_3(list_a):
    list_new = list_a[:5]
    list_b = list_a[2:]

    print(list_a)
    print(list_new)
    print(list_b)

def example_4():
    message = "Don't Subscribe!"
    print(message)
    print(message[6:])
    print(message[6:].upper())

def example_5(list_a):
    print(list_a[-5:-2]) # [6,7,8]

def example_6(list_a):
    print(list_a[-2:-5])  # []

def example_7(list_a):
    print(list_a[::2])

def example_8(list_a):
    print(list_a[::-1])

def example_9(list_a):
    print(list_a[8:2:-1]) # [9,8,7,6,5,4]

def example_10(list_a):
    print(list_a[8:2:-2]) # [9,7,5]

example_10(example_1())