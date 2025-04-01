# Задача 1: Напишіть функцію sub_numbers, яка приймає два аргументи num1 та num2 і повертає їхню різницю.
def sub_numbers(num_1, num_2):
    result = num_1 - num_2
    return result


# Задача 2: Напишіть функцію check_even_odd, яка приймає число number і повертає рядок "Even", якщо число парне,
# і "Odd", якщо число непарне.
def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
    return 0


# Задача 3: Напишіть функцію find_max, яка приймає три числа num1, num2, та num3 і повертає найбільше з них.
def find_max(num_1, num_2, num_3):
    list_of_nums = [num_1, num_2, num_3]
    list_of_nums.sort(reverse=True)
    max_num = list_of_nums[0]

    return max_num


