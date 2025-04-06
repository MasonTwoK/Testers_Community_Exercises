# Задача 1: Створіть кортеж рядків і виведіть перший та останній елементи.
# Виведіть їх за допомогою функції print на екран.
tuple_of_strings = ("Python is awesome!", "Hello World!", "That's the spirit.")

print(tuple_of_strings[0])
print(tuple_of_strings[-1])

# Задача 2: Створіть кортеж і пройдіться по його елементах за допомогою циклу.
# Виведіть кожен елемент на екран за допомоги функції print.
tuple_of_numbers = 1, 2, 3
for tuple_element in tuple_of_numbers:
    print(tuple_element)

# Задача 3: Знайдіть мінімальне та максимальне значення в кортежі чисел. Виведіть результат за допомогою функції print.
tuple_of_numbers = 1, 2, 3
print(f"Tuple of numbers contains: {tuple_of_numbers}")
print(f"Maximal value of tuple is {max(tuple_of_numbers)}")
print(f"Minimal value of tuple is {min(tuple_of_numbers)}")


# **Додаткові завдання:**
# Задача 4:
# Попросіть в користувача ввести два кортежа де будуть тільки слова, збережіть їх у зміні.
# Утворюють використовуючи ці дві зміні третю зміну яка буде містити два попередніх кортежа.
# Тепер розділіть цих два кортежи на перший в якому будуть тільки слова до п'яти букв включно
# та другий де будуть слова більше п'яти букв.
list_result_1 = []
list_result_2 = []

words_1 = input("Введіть перший кортеж: ")
tuple_1 = tuple(words_1.split(' '))

words_2 = input("Введіть другий кортеж: ")
tuple_2 = tuple(words_2.split(' '))

total_tuple = tuple_1 + tuple_2

for word in total_tuple:
    if len(word) <= 5:
        list_result_1.append(word)
    else:
        list_result_2.append(word)

result_1 = tuple(list_result_1)
result_2 = tuple(list_result_2)
