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
string = ''
lowered_words = []
counter = 0
list_of_word = string.split(' ')

for word in list_of_word:
    lowered_words.append(word.lower())

user_input = input('Вкажіть слово: ')
user_input_lowered = user_input.lower()

for word in lowered_words:
    if user_input_lowered == word:
        counter += 1


# Задача 5: До вас звернувся ваш друг тестувальник за допомогою,
# в нього є набір юрлів де потрібно автоматично міняти юрл з prod на qa тобто з ось такої стрічки:
# 'https://prodtea.com.ua ,  https://prod_dim.com.ua'
# потрібно зробити ось таку
# 'https://qatea.com.ua ,  https://qa_dim.com.ua'
