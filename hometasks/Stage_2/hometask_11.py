# Задача 1 Створіть список з довільних чисел і виведіть його елементи, починаючи з другого елементу та з кроком 2.
numbers = list(input("Enter numbers: "))
result = f"Slice of numbers starting second element with step 2: {numbers[1::2]}"
print(result)

# Задача 2 Створіть рядок зі слів "Python is awesome!" і виведіть тільки слово "awesome" у верхньому регістрі з використанням зрізу.
string = "Python is awesome!"
result = string[10:17].upper()
print(result)

# Задача 3 Перевірка на паліндром
# (Паліндром - це слово, яке читається однаково зліва направо та справа наліво, наприклад, "радар" чи "кайак".)
# Напишіть програму яка приймає слово у користувача та за допомогою зріза, перевірте, чи є цей рядок паліндромом.
# Використовуйте assert для перевірки результату:
# якщо рядок є паліндромом, то assert має пройти; якщо ні, має бути виведено відповідне повідомлення про помилку.
def task_3(entered_string): assert entered_string == entered_string[::-1], "Entered string is not palindrome"