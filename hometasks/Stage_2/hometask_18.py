# Задача 1: Створіть функцію, яка друкує привітання для користувача.
def foo_1():
    user_name = input('Enter user name: ')
    print('Hello', user_name)


# Задача 2: Створіть функцію для обчислення суми двох чисел що запитує їх у користувача і друку результату
def foo_2():
    number_1 = int(input('Enter first number: '))
    number_2 = int(input('Enter second number: '))

    result = number_1 + number_2
    print(result)


# Задача 3: Створіть функцію  яка просить користувача створити список чисел
# та розрахуйте середнє значення списку чисел і друку результат
def foo_3():
    sequence_of_number = input('Enter sequence of numbers (with space between them): ')
    list_of_numbers = sequence_of_number.split(' ')

    sum_of_numbers = 0
    for number in list_of_numbers:
        sum_of_numbers += int(number)

    result = sum_of_numbers / len(list_of_numbers)
    print(result)
