# Задача 1 Лічильник до 10: Напишіть програму, яка використовує цикл while для виведення чисел від 1 до 10.
def task_1():
    i = 0
    while i < 10:
        print(i)
        i+=1

# Задача 2 Сума чисел: Напишіть програму, яка використовує цикл while для підрахунку суми чисел від 1 до 100.
def task_2():
    print("App that provides Triangular number")
    entered_number = int(input("Enter your number: "))

    iterator = 1
    nums_sum = 0

    while iterator <= entered_number:
        nums_sum += iterator
        iterator += 1

    print(f"Triangle numbers of {entered_number} is {nums_sum}")

# Задача 3 Зворотній відлік:
# Напишіть програму, яка використовує цикл while для виведення зворотного відліку від 10 до 1,
# після чого виводить "Старт!"
def task_3():
    countdown_num = 10

    while countdown_num > 0:
        print(countdown_num)
        countdown_num -= 1
