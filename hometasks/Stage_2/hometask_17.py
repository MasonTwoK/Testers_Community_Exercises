# Задача 1: Напишіть програму, яка запитує у користувача суму в одній валюті (наприклад, долари)
# та конвертує її в іншу валюту (наприклад, євро), використовуючи поточний курс обміну.
# Якщо користувач вибирає USD, конвертувати в EUR; якщо вибирає EUR, конвертувати в USD.
option_text = """Select conversion operation option..
Press button "1" for converting USD to EUR
Press button "2" for converting EUR to USD\n
Enter your option:"""

print('Welcome to currency USD/EUR, EUR/USD converter app!\n')
option_choice = input(option_text)
amount_of_currency = input(f'Enter amount of money: ')
if option_choice == '1':
    result = float(amount_of_currency) * 0.92
elif option_choice == '2':
    result = float(amount_of_currency) * 1.08

print(result)


# Задача 2: Напишіть програму, яка приймає температуру в градусах Цельсія
# і виводить повідомлення про стан води (рідка, тверда, газоподібна) в залежності від введеної температури.
water_states = ("рідка", "тверда", "газоподібна")
temp_c = float(input("Enter water temperature in Celsius: "))  # TODO: add input check
if temp_c >= 100:
    print(water_states[2])
elif 0 < temp_c < 100:
    print(water_states[0])
else:
    print(water_states[1])


# Задача 3: Напишіть програму, яка приймає масу тіла і його швидкість, та визначає його кінетичну енергію.
# Потім виведіть повідомлення про ступінь руху об'єкта (спокій, повільний рух, швидкий рух)
# за допомогою умовної конструкції. (Розрахунок кінетичної енергії за формулою E_kin = 0.5 * m * (v**2))
kinetic_object_states = ('спокій', 'повільний рух', 'швидкий рух')

m = float(input('Enter mass of kinetic object: '))
v = float(input('Enter speed of kinetic object: '))

E_kin = 0.5 * m * (v**2)

if float(E_kin) == 0:
    print(kinetic_object_states[0])
elif 0 < float(E_kin) < 100:
    print(kinetic_object_states[1])
elif float(E_kin) >= 100:
    print(kinetic_object_states[2])
# TODO: What E_kin value should be considered as slow?
# TODO: Next line should be added to this logic:
# else: print('Energy cannot be negative')


# **Додаткові завдання:**
# Задача 4: Напишіть програму, яка використовує програму рандом, що б додати два числа,
# показує цей приклад користувачу(без відповіді),
# якщо користувач відповів правильно вітаємо його,
# якщо неправильно і його відповідь менше правильної то говоримо що відповідь повинна бути більше,
# якщо ж його число більше за відповідь то говоримо що відповідь повинна бути менша.
answer = 4
user_answer = int(input('2 + 2 = '))
if user_answer == answer:
    print('Вітаємо! Ви відповіли правильно.')
elif user_answer < answer:
    print('Відповідь повинна бути більша.')
elif user_answer > answer:
    print('Відповідь повинна бути менша.')

