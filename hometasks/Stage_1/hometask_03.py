# Задача 1: Попросіть користувача ввести рядок і перевірте,
# чи є заданий рядок порожнім, конвертувавши його в булеве значення.
def task_1():
    input_string = bool(input("Insert your string: "))
    assert input_string, 'Inserted string was empty.'

    print("input_string converted to bool type is", input_string)

# Задача 2: Попросіть користувача ввести три числа, які в сумі дають 100, і перевірте це за допомогою assert.
# Якщо користувач ввів неправильно, виведіть йому помилку з написом на ваш розсуд.
def task_2():
    print("Welcome to Total in 100..")

    num_1 = int(input("Enter your 1st number: "))
    num_2 = int(input("Enter your 2nd number: "))
    num_3 = int(input("Enter your 3rd number: "))

    total = num_1 + num_2 + num_3
    assert total == 100, 'Total is not equal to 100'

    print("Total equals ", total)

# Задача 3:Користувач повинен ввести пароль двічі для підтвердження.
# Необхідно перевірити, чи обидва введені паролі співпадають.
# Якщо паролі співпадають, вивести повідомлення 'пароль вірний'.
# Якщо паролі не співпадають, користувач отримує помилку.
def task_3():
    pass_a = input("Enter first password: ")
    pass_b = input("Enter second password: ")

    assert pass_a == pass_b, "Passwords are different."
    print("Check is complete. Passwords are same.")
