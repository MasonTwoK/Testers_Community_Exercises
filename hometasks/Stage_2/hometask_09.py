# Задача 1: Напишіть програму, яка виводить на екран повідомлення про температуру зараз,
# якщо відомо місце проживання і температура у градусах Цельсія.
# Виведіть це у форматі "У місті [місце] зараз [температура] градусів Цельсія".
location = input("Enter your location: ")
temperature = input("Enter temperature outside: ")

print(f"У місті {location} зараз {temperature} градусів Цельсія")

# Задача 2
# Напишіть програму, яка приймає від користувача три рядки: ім'я, вік і місце проживання. Виведіть ці дані у вигляді:
# Ім'я: [ім'я користувача], Вік: [вік користувача] років, Місце проживання: [місце проживання користувача]
name = input("Enter user name: ")
age = input("Enter user age: ")
location = input("Enter location: ")

print("Ім'я: {}, Вік: {} років, Місце проживання: {}".format(name, age, location))

# Задача 3
# Напишіть програму, яка приймає від користувача довжину сторін прямокутника та обчислює його периметр і площу.
# Виведіть результат у такому форматі:
# Довжина: [довжина сторони], Ширина: [ширина сторони], Периметр: [значення периметра], Площа: [значення площі]
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

perimeter = (length + width) * 2
area = length * width

print("Довжина: " + str(length) + ", Ширина: " + str(width) + ", Периметр: " + str(perimeter) + ", Площа: " + str(area))


# **Додаткові завдання:**
# Задача 4
# До вас знов звернулась ваша подруга Марина та просить вас допомогти з анкетними даними для учнів.
# Отже вам потрібно запитати в користувача ось такі дані.
# Ім'я, прізвище, клас, день та місяць народження, улюблений предмет.
# Ім'я та Прізвище повинно бути у верхньому регістрі, а от предмет завжди у нижньому.
# Для оформлення цієї задачі вам потрібно використати f-string

