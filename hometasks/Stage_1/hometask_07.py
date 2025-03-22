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
