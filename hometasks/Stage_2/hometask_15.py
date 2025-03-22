# Задача 1: Напишіть програму, що створює словник для конвертації валют,
# де ключами є валютні коди (наприклад, USD, EUR), а значеннями - курс обміну до гривні.
currencies = ['USD', 'EUR', 'GBP']
list_of_pairs = []

for currency in currencies:
    rate = input(f"Enter rate for {currency} currency: ")
    exchange_pair = [currency, rate]
    list_of_pairs.append(exchange_pair)

currencies_exchange = dict(list_of_pairs)


# Задача 2: Уявімо, що ми маємо список предметів, і нам потрібно створити словник, де кожен предмет буде ключем,
# а початкове значення для кожного ключа буде встановлене як певна оцінка (наприклад, 0).
list_of_items = ['spoon', 'fork', 'knife']
dict_of_items = dict.fromkeys(list_of_items, 0)

# Задача 3: Напишіть програму для створення словника, де ключами будуть імена студентів, а значеннями - їхні середні бали

# Why developers left defined values at the top of method/function?
students_list = []
sum_of_student_marks = 0

student_switch = True
while student_switch:
    student_name = input("Enter student name: ")
    student_marks = input("Enter: student marks: ")

    list_of_student_marks = student_marks.split(' ')
    for mark in list_of_student_marks:
        sum_of_student_marks += int(mark)

    avg_student_mark = sum_of_student_marks / len(list_of_student_marks)
    students_list.append([student_name, avg_student_mark])

    print("Do you want add more students?")
    additional_student_switch = True
    while additional_student_switch:
        decision = input("Enter 1. - Yes, 0. - No.. Enter your choice: ")
        if decision == '1':
            student_switch = True
            additional_student_switch = False
        if decision == '0':
            student_switch = False
            additional_student_switch = False
        else: print("Incorrect input. Try again..")

dict_of_students = dict(students_list)
