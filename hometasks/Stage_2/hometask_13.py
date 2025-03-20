# Задача 1: У вас є 77 задач і 13 людей. Ви хочете розподілити задачі порівну між усіма людьми.
# Напишіть програму, яка визначить, скільки задач отримає кожна людина, і скільки задач залишиться нерозподіленими.
def task_1():
    tasks = 77
    people = 13

    tasks_per_person = tasks // people
    print(f"Amount tasks for each person: {tasks_per_person}")

    tasks_in_backlog = tasks % people
    print(f"Tasks in back log left: {tasks_in_backlog}")

# Задача 2: Віктор займається фотографією. Він вирішив зібрати всі свої 168 фотографії та вклеїти в альбом.
# На одній сторінці може бути розміщено щонайбільше 8 фото. Скільки сторінок знадобиться Ігорю, щоб вклеїти всі фото?
def task_2():
    photos = int(input("Enter amount of photos: "))
    photos_per_page = 8

    amount_of_pages = photos // photos_per_page
    if (photos % photos_per_page) > 0: print(f"Amount of pages required in album: {amount_of_pages + 1}")
    else: print(f"Amount of pages required in album: {amount_of_pages}")

# Задача 3
# Стас і Маша вирішили скористатися послугою «Оплата частинами» для придбання комп'ютера.
# Вони знають загальну вартість комп'ютера (45999 грн) та розмір місячного платежу (7500 грн).
# Ваше завдання - допомогти їм визначити, скільки місяців їм потрібно буде платити, щоб повністю розрахуватися за комп'ютер.
# Виведіть це число користувачу для його зручності та кращого розуміння умови оплати.
def task_3():
    pc_price = 45999
    payment = 7500

    amount_of_months = pc_price // payment
    remained_amount = pc_price % payment

    for month_number in range(amount_of_months): print(f"For month {month_number + 1} payment is {payment}")
    print(f"For month {amount_of_months + 1} payment is {remained_amount}")
