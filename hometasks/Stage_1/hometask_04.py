# Задача 1: Створіть програму, яка запитує у користувача його вік.
# Якщо вік користувача менше 18 років, програма повинна вивести "Ви ще надто молоді",
# якщо вік рівний або більше 18 років, то повинна вивести "Ласкаво просимо!".
print("Вітаю у додатку, що перевіряє вік!")
age = int(input("Введіть свій вік: "))

if age < 18:
    print("Ви ще надто молоді")
if age >= 18:
    print("Ласкаво просимо!")

# Задача 2: Напишіть програму, яка порівнює дві змінні: temperature_outside та temperature_comfort.
# Якщо temperature_outside вище temperature_comfort, виведіть "Увімкніть кондиціонер".
# Якщо нижче, виведіть "Можливо, вам буде комфортно без кондиціонера".
temper_outside = float(input("Введіть темпаратуру на вулиці: "))
temper_comfort = float(input("Введіть комфортну температуру: "))

if temper_outside > temper_comfort:
    print("Увімкніть кондиціонер")
else:
    print("Можливо, вам буде комфортно без кондиціонера")


# Задача 3: напишіть студентські тести по математиці де ви даєте приклад і користувач вводе відповідь,
# а ви йому відповідаєте вірно він вирішив задачу чи ні. Зробіть 3-5 прикладів.
print("Welcome to math exam program.")
result = int(input("Task #1: 2+2="))
if result == 4:
    print("Answer is correct!")
else:
    print("Answer is wrong. Right answer is 4")

result = int(input("Task #2: 3*5="))
if result == 15:
    print("Answer is correct!")
else:
    print("Answer is wrong. Right answer is 15")

result = int(input("Task #3: 21/3="))
if result == 7:
    print("Answer is correct!")
else:
    print("Answer is wrong. Right answer is 7")


# Задача 4: Пам'ятаєте задачу з попереднього уроку, про вашу подругу вчительку.
# Тепер Ви можете покращити цю програму використовуючи if, else.
# Умова задачі:
# * Питань повинно бути п'ять, питання виглядають в такому вигляді на екрані з'являється слово написане
# українською мовою і студент має ввести його переклад на англійській мові.
# * Якщо переклад правильний він отримує плюс один бал і повідомлення що він вірно відповів.
# * Якщо ж відповідь неправильна. то він не отримує балів, але отримує повідомлення що відповідь не правильна
# і йде до настпуного питання.
# * В кінці тесту ви виводите кількість балів. І дякую за приділений час.
score = 0

translate = input("ручка\n")
if translate == "pen":
    score += 1
    print("Answer is correct")
else:
    print("Answer is wrong")

translate = input("олівець\n")
if translate == "pencil":
    score += 1
    print("Answer is correct")
else:
    print("Answer is wrong")

translate = input("зошит\n")
if translate == "notebook":
    score += 1
    print("Answer is correct")
else:
    print("Answer is wrong")

translate = input("стіл\n")
if translate == "table":
    score += 1
    print("Answer is correct")
else:
    print("Answer is wrong")

translate = input("стілець\n")
if translate == "chair":
    score += 1
    print("Answer is correct")
else:
    print("Answer is wrong")

print(str(score) + " Дякую за приділений час")
