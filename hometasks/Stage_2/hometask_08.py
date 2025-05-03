# Задача 1: Напишіть програму, яка приймає рядок від користувача і виводить його у верхньому регістрі.
entered_string = input("Enter you string: ")
result = entered_string.upper()
print(result)

# Задача 2: Створіть програму, яка приймає рядок від користувача та заміняє всі входження символу 'a' на '*',
# якщо символ ‘а’ відсутній до відповідне повідомлення.
entered_string = input("Enter the string: ")

list_of_letters = []
for letter in entered_string:
    list_of_letters.append(letter)

base_list_of_letters = list_of_letters.copy()

counter = 0
for letter in list_of_letters:
    if not letter.find('a') == -1:
        list_of_letters[counter] = letter.replace('a', '*')
        counter += 1
        continue
    if not letter.find('A') == -1:
        list_of_letters[counter] = letter.replace('A', '*')
        counter += 1
        continue
    if not letter.find('а') == -1:
        list_of_letters[counter] = letter.replace('а', '*')
        counter += 1
        continue
    if not letter.find('А') == -1:
        list_of_letters[counter] = letter.replace('А', '*')
        counter += 1
        continue
    counter += 1

if list_of_letters == base_list_of_letters:
    print("Characters 'A' and 'a' are missing in entered string")
else:
    result = ''.join(list_of_letters)
    print(result)

# 8.2 Rework
# Задача 2: Створіть програму, яка приймає рядок від користувача та заміняє всі входження символу 'a' на '*',
# якщо символ ‘а’ відсутній до відповідне повідомлення.
user_string = input("Введіть слово")

result = user_string.replace('a', '*').replace('A', '*').replace('а', '*').replace('А', '*')
if result != user_string:
    print(result)
else:
    print("символ ‘а’ відсутній до відповідне повідомлення.")


# 8.2 dict data type rework
# Задача 2: Створіть програму, яка приймає рядок від користувача та заміняє всі входження символу 'a' на '*',
# якщо символ ‘а’ відсутній до відповідне повідомлення.
default_user_string = input("Введіть слово")
dict_a = {
    'a': '*',
    'A': '*',
    'а': '*',
    'А': '*'
}

starred_user_string = default_user_string
for key in dict_a.keys():
    if key in starred_user_string:
        result = starred_user_string.replace(key, dict_a.get(key))
        starred_user_string = result

if starred_user_string != default_user_string:
    print(starred_user_string)
else:
    print("'a' symbol is missing in user string")


# Задача 3: Напишіть програму,
# яка приймає рядок від користувача та виводить його з позначенням кількості символів у ньому.
entered_string = input("Enter string: ")
print(f"Entered string: {entered_string}")

length_of_string = len(entered_string)
print(f"Length of string by using length method: {length_of_string}")

# **Додаткові завдання:**
# Задача 4: Напишіть програму яка перевіряє рядок на вказане користувачем слово
# і підраховує скільки разів воно зустрічається, якщо слово зустрічається в різному регістрі ви рахуєте його два рази.
# Тобто слів "Хліб" та слово "хліб" це одне і теж слово.
base_text = """I come and I go
Tell me all the ways you need me
I'm not here for long
Catch me or I go Houdini
I come and I go
Prove you got the right to please me
Everybody knows
Catch me or I go Houdini"""

user_input = input('Вкажіть слово: ')
result = base_text.lower().count(user_input.lower())
print(result)

# Задача 5: До вас звернувся ваш друг тестувальник за допомогою,
# в нього є набір юрлів де потрібно автоматично міняти юрл з prod на qa тобто з ось такої стрічки:
# 'https://prodtea.com.ua ,  https://prod_dim.com.ua'
# потрібно зробити ось таку
# 'https://qatea.com.ua ,  https://qa_dim.com.ua'
prod_url_tuple = ('https://prodtea.com.ua', 'https://prod_dim.com.ua')
qa_url_list = []

for prod_url in prod_url_tuple:
    qa_url = prod_url.replace('prod', 'qa')
    qa_url_list.append(qa_url)
