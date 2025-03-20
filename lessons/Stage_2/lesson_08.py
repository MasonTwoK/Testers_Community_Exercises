
def example_1():
    our_string = "Hello World!"

    print(our_string)
    print(our_string.upper())
    print(our_string.lower())

    print(our_string.count('l'))
    print(our_string.count('ll'))
    print(our_string.count("l", 3))
    print(our_string.count('l', 3, 7))
    print(our_string.find("Wor"))
    print(our_string.find('o'))
    print(our_string.rfind('o'))
    print(our_string.find("There is no such sequence"))
    # print(our_string.index("There is no such sequence"))
    print(our_string.replace("Hello", "Hi"))
    print(our_string.replace(" ", ""))
    print(our_string.isalpha())
    print("something".isalpha())
    print(our_string.isdigit())
    print("123".isdigit())
    print("text".rjust(10))
    print("message".rjust(10, "!"))
    print("message".ljust(10, "!"))

    new_string = "   Hey Brother   "
    print(new_string.strip())
    print(new_string.lstrip())
    print(new_string.rstrip())

example_1()