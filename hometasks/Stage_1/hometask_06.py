# Задача 1
# Написати цикл for,
# який обраховує суму всіх чисел у списку numbers = [1, 2, 3, 4, 5].
def task_1():
    nums_list = [1,2,3,4,5]
    nums_sum = 0

    for iterator in nums_list:
        nums_sum += iterator

    print(f"Values in list: {nums_list}")
    print(f"Sum of all numbers in list: {nums_sum}")


# Задача 2
# Використовуючи цикл for,
# напишіть код, який ітерує по списку numbers = [-2, -1, 0, 1, 2] і виводить тільки позитивні числа.
def task_2():
    nums_list = [-2, -1, 0, 1, 2]

    for iterator in nums_list:
        if iterator > 0:
            print(iterator)


# Задача 3
# Використовуючи цикл for,
# створіть новий список, що містить квадрати всіх чисел у вихідному списку numbers = [1, 2, 3, 4, 5].
def task_3():
    nums_list = [1, 2, 3, 4, 5]
    pows_list = []

    for iterator in nums_list:
        pows_list.append(iterator * iterator)

    print(f"List with nums: {nums_list}")
    print(f"List with pows: {pows_list}")
