# Задача 1
d = {'name': 'John Doe', 'age': 30,
     'city': 'New York',
     'email': 'johndoe@example.com'}
# Попросіть користувача ввести ключ, який він бажає видалити, і видаліть цей елемент зі словника.
# Та виведіть на екран змінений словник.

# while True:
#     key = input("Enter the key of pair you want to delete: ")
#
#     if key in d.keys():
#         d.pop(key)
#         print(d)
#         break
#     else:
#         print("Wrong key was entered! Try again..")


# Задача 2
d = {'name': 'Alice Smith',
     'age': 25, 'city': 'Los Angeles',
     'email': 'alice.smith@example.com',
     'favorite_subjects': ['Mathematics', 'History', 'Literature']}
# Виведіть з цього словника значення 'favorite_subjects' використовуючи цикл.
for values in d['favorite_subjects']:
    print(values)


# Задача 3
favorites = {
    'movies': ['Interstellar', 'Fast & Furious', 'Pirates of the Caribbean'],
    'music': ['Queen', 'The Beatles', 'Coldplay'],
    'sports': ['football', 'basketball', 'tennis']}
# Видаліть з цього списку sports та додайте новий ключ 'serials' де значенням будуть ваші улюблені серіали.
favorites.pop('sports')
favorites.update({'serials': ['Invincible', 'Netrunner', 'Berserk', 'Blue Eyed Samurai']})


# Додаткові завдання:
# Задача 4: Памятаєте ми з вами в попередньому уроці робили записник контактів.
# Тепер ми його покращимо. За допомогою циклу while.
# Реалізуйте такі опції в вашому Записнику:
# Додати новий контакт
# Подивитись контакт
# Оновити старий контакт
# Видалити контакт
# Доречи ці чотири операції входять в основні функції управління даними CRUD(Create, Read, Update, Delete).
# Про CRUD ви напевно вже чули, а якщо ні то ще будете чути дуже багато разів.
contacts = {
    "Коваленко": ['19 Березня', 'Київ', ['+380 67 716 13 46', 'kovalenko.t@gmail.com']],
    "Промський": ['10 Червня', 'Миколаїв', ['+380 50 202 15 22', 'markymark@gmail.com']],
    "Головарьова": ['22 Липня', 'Донецьк', ['+380 63 117 48 91', 'anna.holovarova1994@gmail.com']]
}


def contacts_welcome_dialog():
    welcome_dialog_text = """Виберіть число згідно опцій роботи з контактами:\n1 - Додати новий контакт\n2 - Подивитись контакт\n3 - Оновити старий контакт\n4 - Видалити контакт"""
    print(welcome_dialog_text)

    return 0


def contacts_keys_presenter(dict_contacts):
    for key in dict_contacts.keys():
        print(key)
    while True:
        key = input("Виберіть імʼя (прізвище) конткату з переліку, що вище: ")
        if key in contacts.keys():
            break
        else:
            print("Помилка! Імʼя (прізвища), що ви ввели не має в переліку контактів..")

    return key


def contacts_create_contact():
    contacts_key = input("Введіть імя (прізвище) контакту: ")

    value_birth_date = input("Введіть день народження контакту: ")
    value_city = input("Введіть місто конткакту: ")
    value_phone = input("Введіть телефон контакту: ")
    value_email = input("Введіть електронну пошту контакту: ")
    contacts_value = [value_birth_date, value_city, [value_phone, value_email]]

    contacts.update({contacts_key: contacts_value})

    return 0


def contacts_update_existed_contact(contact_value):
    while True:
        update_existed_contact_dialog = """1 - Дата народження\n2 - Місто\n3 - Телефон\n4 - Електронна пошта"""
        print(update_existed_contact_dialog)

        user_selection = input("Введіть номер поля, яке ви хочете змінити: ")
        if user_selection == '1':
            contact_value[0] = input("Введіть новий день народження контакту: ")
            break
        elif user_selection == '2':
            contact_value[1] = input("Введіть нове місто контакту: ")
            break
        elif user_selection == '3':
            contact_value[2][0] = input("Введіть новий телефон контакту: ")
            break
        elif user_selection == '4':
            contact_value[2][1] = input("Введіть нову електронну пошту контакту: ")
            break
        else:
            print("Не вірний ввід ввід.. Спробуйте ще раз")

    contacts.update({contact_key: contact_value})


contacts_welcome_dialog()
while True:
    user_answer = input("Введіть ваш вибір: ")

    if user_answer == '1':
        contacts_create_contact()
        break

    elif user_answer == '2':
        contacts_key = contacts_keys_presenter(contacts)
        result = contacts.get(contacts_key)

        print(result)
        break

    elif user_answer == '3':
        contact_key = contacts_keys_presenter(contacts)
        contact_value = contacts.get(contact_key)

        contacts_update_existed_contact(contact_value)
        break

    elif user_answer == '4':
        contacts_key = contacts_keys_presenter(contacts)
        contacts.pop(contacts_key)
        break

    else:
        print("Не вірний ввід ввід.. Спробуйте ще раз")
