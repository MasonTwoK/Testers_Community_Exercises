# Задача 1: Напишіть програму, яка приймає рядок від користувача і виводить його у верхньому регістрі.
def task_1():
    entered_string = input("Enter you string: ")
    print(entered_string.upper())

# Задача 2: Створіть програму, яка приймає рядок від користувача та заміняє всі входження символу 'a' на '*',
# якщо символ ‘а’ відсутній до відповідне повідомлення.
def task_2():
    entered_string = input("Enter the string: ")
    if entered_string.find('a') == -1:
        print(" 'a' character is missing in entered string")
    else:
        print(entered_string.replace('a', '*'))

# Задача 3: Напишіть програму, яка приймає рядок від користувача та виводить його з позначенням кількості символів у ньому.
def task_3():
    entered_string = input("Enter string: ")
    print(f"Entered string: {entered_string}")

    print(f"Length of string by using length method: {len(entered_string)}")