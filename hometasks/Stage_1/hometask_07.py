# Задача 1 Лічильник до 10: Напишіть програму, яка використовує цикл while для виведення чисел від 1 до 10.
i = 0
while i < 10:
    print(i + 1)
    i += 1

# Задача 2 Сума чисел: Напишіть програму, яка використовує цикл while для підрахунку суми чисел від 1 до 100.
print("App that provides Triangular number of 100")
iterator = 1
nums_sum = 0

while iterator <= 100:
    nums_sum += iterator
    iterator += 1

print(f"Triangular numbers of 100 is {nums_sum}")

# Задача 3 Зворотній відлік:
# Напишіть програму, яка використовує цикл while для виведення зворотного відліку від 10 до 1,
# після чого виводить "Старт!"
countdown_num = 10
while countdown_num > 0:
    print(countdown_num)
    countdown_num -= 1


# **Додаткові завдання:**
# Задача 4: Цього разу Ви вирішили написати Гру. Ви загадуєте число і користувач намагається його вгадати вводячи дані.
# Якщо він ввів менше загаданого числа то ви виводите повідомлення "Загадане число більше ніж ви вказали"
# і відповідно якщо він ввів менше то ви пишете "Загадане число менше ніж ви вказали""
# Коли користувач відгадає число, виведіть кількість спроб яку він використав та привітайте його з виграшом.
secret_number = 1
attempt_counter = 0
user_number = None

while not secret_number == user_number:
    user_number = int(input("Введіть своє число: "))
    attempt_counter += 1
    if user_number < secret_number:
        print("Загадане число більше ніж ви вказали")
    if user_number > secret_number:
        print("Загадане число менше ніж ви вказали")

message_congrats = "\nВітаю, ви відгадали!"
message_attempt = "Кількість використаних спроб: "
result = message_attempt + str(attempt_counter) + message_congrats

print(result)
