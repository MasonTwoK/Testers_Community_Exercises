class Example1:
    def foo(self, a):
        return a ** 3

    lambda_f1 = lambda x: x ** 3


class Example2:
    def foo_2(self, number):
        if number % 2 == 1:
            return 'NO'
        else:
            return 'YES'

    lambda_f2 = lambda number: 'no' if number % 2 == 1 else 'yes'  # I do not see logic in expression


def example_3():
    list_a = [199, 2, 34, 909, -100, 18]
    print(list_a)

    list_a.sort(key=lambda x: x % 10)  # I do not understand who 'key=' works in this case
    print(list_a)


def example_4():
    calculator = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }

    result = calculator['+'](1, 2)  # I do not think that was in lesson 15 & 16
    print(result)

