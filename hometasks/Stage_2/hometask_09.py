# Задача 1: Напишіть програму, яка виводить на екран повідомлення про температуру зараз,
# якщо відомо місце проживання і температура у градусах Цельсія.
# Виведіть це у форматі "У місті [місце] зараз [температура] градусів Цельсія".
def task_1():
    location = input("Enter your location: ")
    temperature = input("Enter temperature outside: ")

    print("Location: " + location + ". Temperature = " + temperature + " (Concatenation)")
    print(f"Location: {location}. Temperature = {temperature} (f_string)")
    print("Location: {}. Temperature = {} (formatted string)".format(location,temperature))

# Задача 2
# Напишіть програму, яка приймає від користувача три рядки: ім'я, вік і місце проживання. Виведіть ці дані у вигляді:
# Ім'я: [ім'я користувача], Вік: [вік користувача] років, Місце проживання: [місце проживання користувача]
def task_2():
    name = input("Enter user name: ")
    age = input("Enter user age: ")
    location = input("Enter location: ")

    print(f"Name: {name}, age = {age}, location: {location}. (f_string)")
    print("Name: {}, age = {}, location: {}. (formatted string)".format(name, age, location))
    print("Name: " + name + ", age = " + age + ", location: " + location + ". (concatenate)")

# Задача 3
# Напишіть програму, яка приймає від користувача довжину сторін прямокутника та обчислює його периметр і площу.
# Виведіть результат у такому форматі:
# Довжина: [довжина сторони], Ширина: [ширина сторони], Периметр: [значення периметра], Площа: [значення площі]

def task_3():
    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))

    perimeter = (length + width) * 2
    area = length * width

    print(f"Length = {length}, Width = {width}, Perimeter = {perimeter}, Area = {area}. (f_string)")
    print("Length = {}, Width = {}, Perimeter = {}, Area = {} (formatted string)".format( length, width, perimeter, area))
    print("Length = " + str(length) + ", Width = " + str(width) + ", Perimeter = " + str(perimeter) + ", Area = " + str(area) + " (concatenation)")
