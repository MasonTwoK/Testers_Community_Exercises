# Задача 1: Створіть змінну з текстом і виведіть її на екран за допомогою функції print.
value_text = "Value with text."
print(value_text)


# Задача 2: Створіть ще одну змінну, але вже з числом і виведіть її на екран за допомогою функції print.
value_int = 10
print(value_int)


# Задача 3: Виведіть на екран за допомогою функцій type та print тип двох змінних з задачі один та задачі два.
text_type = type(value_text)
print(text_type)

int_type = type(value_int)
print(int_type)

# Задача 4: Вам потрібно створити зміну яка буде зберігати вік,
# але умова така що далі ця зміна буде використовуватись програмою яка працює тільки з типом даних str.
# Вирішіть проблему. Та виведіть тип змінної та її результат.
age = 21
str_value = str(age)
value_type = type(str_value)
print(value_type, str_value)
