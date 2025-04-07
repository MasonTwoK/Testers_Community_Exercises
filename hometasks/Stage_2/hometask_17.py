# Задача 1: Напишіть програму, яка запитує у користувача суму в одній валюті (наприклад, долари)
# та конвертує її в іншу валюту (наприклад, євро), використовуючи поточний курс обміну.
# Якщо користувач вибирає USD, конвертувати в EUR; якщо вибирає EUR, конвертувати в USD.
option_switch = True
option_choice = 0
exchange_rate = {
    'USD/EUR': 0.92,
    'EUR/USD': 1.08
}
option_message = (
    'Select conversion operation option..',
    'Press button "1" for converting USD to EUR\n',
    'Press button "2" for converting EUR to USD\n',
    'Enter your option: ')
currency = ('USD', 'EUR')

exchange_rate_keys = tuple(exchange_rate.keys())

print('Welcome to currency USD/EUR, EUR/USD converter app!\n')
print(option_message[0])
while option_switch:
    option_choice = input(str(option_message[1] + option_message[2] + option_message[3]))

    if str(1) == option_choice:
        option_switch = False
    elif str(2) == option_choice:
        option_switch = False
    else:
        print("Input incorrect. Select between options '1' & '2'..")

option_choice = int(option_choice)-1  # Is it okay that I resave value like this?
amount_of_currency = input(f'Enter amount of {currency[option_choice]}: ')
result = float(amount_of_currency) * exchange_rate[exchange_rate_keys[option_choice]]


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

