def example_1():
    print("How much does it cost?")
    price = float(input())
    print(price)

    discount = float(input("Which price of your discount?\n"))
    print("Your discount =", discount)

    final_price = price - discount
    print("Final price is", final_price)

def example_2():
    val1 = 9
    val2 = 3

    print(val1 - val2)
    print(val1 * val2)
    print(val1 * val2)
    print(val1 / val2)

    print()

    print(val1 + val1 + val2)

    result_1 = val1 + val1 * val2
    result_2 = (val1 + val1) * val2
    print(result_1)
    print(result_2)

    float_1 = 9.99
    print(type(float_1), float_1)
