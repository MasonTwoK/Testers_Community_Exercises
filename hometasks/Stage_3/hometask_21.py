# Задача 1: Напишіть тести за допомогою assert що б перевірити всі функції з уроку.
# Як використовувати assert Урок 3(Python)
def foo(a):
    return a ** 3


assert foo(2) == 8, 'Result is not equal 8'

lambda_f1 = lambda x: x ** 3
assert lambda_f1(2) == 8, 'Result is not equal 8'


def foo_2(number):
    if number % 2 == 1:
        return 'NO'
    else:
        return 'YES'


assert foo_2(3) == 'NO', "Answer is not equal 'NO'"
assert foo_2(2) == 'YES', "Answer is not equal 'YES'"

lambda_f2 = lambda number: 'no' if number % 2 == 1 else 'yes'
assert lambda_f2(3) == 'no', "Answer is not equal 'no'"
assert lambda_f2(2) == 'yes', "Answer is not equal 'yes'"

list_a = [199, 2, 34, 909, -100, 18]
list_a.sort(key=lambda x: x % 10)
assert list_a == [-100, 2, 34, 18, 199, 909], "List is not sorted from smaller to bigger number"

calculator = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

assert calculator.get('+')(1, 2) == 3, 'Result is not equal 3'
assert calculator.get('-')(2, 1) == 1, 'Result is not equal 1'
assert calculator.get('*')(1, 2) == 2, 'Result is not equal 2'
assert calculator.get('/')(8, 2) == 4, 'Result is not equal 4'

# Задача 2: Напишіть Лямбда функцію яка нічого не приймає, а повертає 'Привіт спільното'
a = lambda: 'Привіт спільнота'
print(a())

# Задача 3: Зробіть лямбда функцію яка перевіряє чи число більше нуля чи менше і виводить повідомлення.
more_or_less_than_zero_message = lambda number: 'Yes' if number > 0 else ('No' if number < 0 else 'Number is zero')
print(more_or_less_than_zero_message(1))
print(more_or_less_than_zero_message(-1))
print(more_or_less_than_zero_message(0))
