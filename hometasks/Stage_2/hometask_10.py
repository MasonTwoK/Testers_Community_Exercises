# Задача 1: Створіть кортеж рядків і виведіть перший та останній елементи. Виведіть їх за допомогою функції print на екран.
def task_1():
    tuple_of_strings = ("Python is awesome!", "Hello World!", "That's the spirit.")

    print(tuple_of_strings[0])
    print(tuple_of_strings[-1])

# Задача 2: Створіть кортеж і пройдіться по його елементах за допомогою циклу. Виведіть кожен елемент на екран за допомоги функції print.
def task_2():
    tuple_of_numbers = 1, 2, 3
    for tuple_element in tuple_of_numbers:
        print(tuple_element)

# Задача 3: Знайдіть мінімальне та максимальне значення в кортежі чисел. Виведіть результат за допомогою функції print.
def task_3():
    tuple_of_numbers = 1, 2, 3
    print(f"Tuple of numbers contains: {tuple_of_numbers}")
    print(f"Maximal value of tuple is {max(tuple_of_numbers)}")
    print(f"Minimal value of tuple is {min(tuple_of_numbers)}")