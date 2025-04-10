# Задача 5
# Дано число. Знайдіть число десятків у його десятковому записі (тобто другу справа цифру його десяткового запису).
number = 583
result = number % 100


# Задача 1: У вас є 77 задач і 13 людей. Ви хочете розподілити задачі порівну між усіма людьми.
# Напишіть програму, яка визначить, скільки задач отримає кожна людина, і скільки задач залишиться нерозподіленими.
tasks = 77
people = 13

tasks_per_person = tasks // people
result = f"Amount tasks for each person: {tasks_per_person}"
print(result)

tasks_in_backlog = tasks % people
result = f"Tasks in back log left: {tasks_in_backlog}"
print(result)


# # Задача 2: Віктор займається фотографією. Він вирішив зібрати всі свої 168 фотографії та вклеїти в альбом.
# # На одній сторінці може бути розміщено щонайбільше 8 фото. Скільки сторінок знадобиться Ігорю, щоб вклеїти всі фото?
photos = 168
photos_per_page = 8

amount_of_pages = photos // photos_per_page
if (photos % photos_per_page) > 0:
    result = f"Amount of pages required in album: {amount_of_pages + 1}"
    print(result)
else:
    result = f"Amount of pages required in album: {amount_of_pages}"
    print(result)


# Задача 3
# Стас і Маша вирішили скористатися послугою «Оплата частинами» для придбання комп'ютера.
# Вони знають загальну вартість комп'ютера (45999 грн) та розмір місячного платежу (7500 грн).
# Ваше завдання - допомогти їм визначити, скільки місяців їм потрібно буде платити,
# щоб повністю розрахуватися за комп'ютер.
# Виведіть це число користувачу для його зручності та кращого розуміння умови оплати.
pc_price = 45999
payment = 7500

amount_of_months = pc_price // payment
remained_amount = pc_price % payment

if remained_amount != 0:
    remained_month = 1
else:
    remained_month = 0

result = f"Стас і Маша повинні платити {amount_of_months + remained_month} місяців"
print(result)


# **Додаткові завдання:**
# Задача 4
# Дано число. Виведіть його останню цифру.
number = 321
result = number % 10
print(result)


# Задача 5
# Дано число. Знайдіть число десятків у його десятковому записі (тобто другу справа цифру його десяткового запису).
number = 12341
result = number % 100
print(result)


# Задача 6
# Дано тризначне число. Знайдіть суму його цифр. Вирішіть цю задачу декількома способами.
# Спосіб 1:
number = 111
total = 0
for number in str(number):
    total += int(number)


# Спосіб 2:
number = 111

number_1 = number % 10
number_2 = ((number % 100) - number_1) / 10
number_3 = (number - (number % 100)) / 100
total = number_3 + number_2 + number_1


# Задача 7
# За день машина проїжджає 𝑛 кілометрів. Скільки днів потрібно, щоб проїхати маршрут довжиною 𝑚 кілометрів?
n = 10
m = 111
result = m // n
if (m % n) != 0:
    result += 1
