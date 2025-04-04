# Задача 1: Попросіть користувача ввести рядок і перевірте,
# чи є заданий рядок порожнім, конвертувавши його в булеве значення.
input_string = bool(input("Insert your string: "))
assert input_string, 'Inserted string was empty.'

print("input_string converted to bool type is", input_string)


# Задача 2: Попросіть користувача ввести три числа, які в сумі дають 100, і перевірте це за допомогою assert.
# Якщо користувач ввів неправильно, виведіть йому помилку з написом на ваш розсуд.
print("Welcome to Total in 100..")

num_1 = int(input("Enter your 1st number: "))
num_2 = int(input("Enter your 2nd number: "))
num_3 = int(input("Enter your 3rd number: "))

assert num_1 + num_2 + num_3 == 100, 'Total is not equal to 100'

# Задача 3:Користувач повинен ввести пароль двічі для підтвердження.
# Необхідно перевірити, чи обидва введені паролі співпадають.
# Якщо паролі співпадають, вивести повідомлення 'пароль вірний'.
# Якщо паролі не співпадають, користувач отримує помилку.
pass_a = input("Enter first password: ")
pass_b = input("Enter second password: ")

assert pass_a == pass_b, "Passwords are different."
print("Check is complete. Passwords are same.")


# Задача 4: До вас звернулась ваша подруга Марина, викладачка англійської мови.
# Вона викладає в новітній обладнаній школі у місті Вінниця, в них є комп'ютери на яких учні можуть проходити тести.
# І ваша задача написати тест який після кожного питання буде виводи кількість балів набраних учнем.
# Питань повинно бути п'ять, питання виглядають в такому вигляді на екрані з'являється слово написане українською мовою
# і студент має ввести його переклад на англійській мові.
# Якщо переклад правильний він отримує плюс один бал, якщо ні то програма повинна зламатись.
# В кінці тесту, тобто після п'ятого питання ви повинні зламати тест(зробіть AssertionError) після виведення балів,
# що б учні не могли ніяк змінити свій результат.
score = 0

translate = input("ручка")
assert translate == "pen"
score += 1
print(score)

translate = input("олівець")
assert translate == "pencil"
score += 1
print(score)

translate = input("зошит")
assert translate == "notebook"
score += 1
print(score)

translate = input("стіл")
assert translate == "table"
score += 1
print(score)

translate = input("стілець")
assert translate == "chair"
score += 1
print(score)

assert False
