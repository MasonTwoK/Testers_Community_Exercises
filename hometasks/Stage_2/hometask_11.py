# Задача 1 Створіть список з довільних чисел і виведіть його елементи, починаючи з другого елементу та з кроком 2.
numbers_string = input("Enter numbers: ")
numbers_list = numbers_string.split(' ')
for index in range(len(numbers_list)):
    int(numbers_list[index])
result = f"Slice of numbers starting second element with step 2: {numbers_list[1::2]}"
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
entered_string = input("Enter palindrome string: ")
assert entered_string == entered_string[::-1], "Entered string is not palindrome"


# **Додаткові завдання:**

# Задача 4
# all letters = 'Жебракують філософи при ґанку церкви в Гадячі, ще й шатро їхнє п'яне знаємо'
# Використовуючи зміну all letters напишіть своє ім'я.
