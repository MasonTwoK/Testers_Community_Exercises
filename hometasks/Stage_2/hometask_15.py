# Задача 1: Напишіть програму, що створює словник для конвертації валют,
# де ключами є валютні коди (наприклад, USD, EUR), а значеннями - курс обміну до гривні.
# currencies_exchange = {
#     'USD': input(f"Enter rate for 'USD' currency: "),
#     'EUR': input(f"Enter rate for 'EUR' currency: ")
# }
#
# # Задача 2: Уявімо, що ми маємо список предметів, і нам потрібно створити словник, де кожен предмет буде ключем,
# # а початкове значення для кожного ключа буде встановлене як певна оцінка (наприклад, 0).
# list_of_items = ['spoon', 'fork', 'knife']
# dict_of_items = dict.fromkeys(list_of_items, 0)

# Задача 3: Напишіть програму для створення словника, де ключами будуть імена студентів, а значеннями - їхні середні бали
# Why developers left defined values at the top of method/function?
students_list = []

main_logic_switch = True
while main_logic_switch:
    student_name = input("Enter student name: ")
    student_marks = input("Enter: student marks: ")

    list_of_student_marks = student_marks.split(' ')

    sum_of_student_marks = 0
    for mark in list_of_student_marks:
        sum_of_student_marks += int(mark)

    avg_student_mark = sum_of_student_marks / len(list_of_student_marks)
    students_list.append([student_name, avg_student_mark])

    print("Do you want add more students?")
    add_student_answer_switch = True
    while add_student_answer_switch:
        answer = input("Enter 1. - Yes, 0. - No.. Enter your choice: ")
        if answer == '1':
            main_logic_switch = True
            add_student_answer_switch = False
        if answer == '0':
            main_logic_switch = False
            add_student_answer_switch = False
        else: print("Incorrect input. Try again..")

dict_of_students = dict(students_list)


# **Додаткові завдання:**
# Задача 4
# Створіть записник де ключе буде прізвище, а значенням такі дані(день народження, місце проживання, та контактні дані)
contacts = {
    "Коваленко": ['19 Березня', 'Київ', ['+380 67 716 13 46', 'kovalenko.t@gmail.com']],
    "Промський": ['10 Червня', 'Миколаїв', ['+380 50 202 15 22', 'markymark@gmail.com']],
    "Головарьова": ['22 Липня', 'Донецьк', ['+380 63 117 48 91', 'anna.holovarova1994@gmail.com']]
}
