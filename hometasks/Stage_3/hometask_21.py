# Задача 1: Створіть клас "MorningGreeter", який містить метод "say_good_morning",
# що виводить повідомлення привітання вашого знаймого з добрим ранком.
class MorningGreeter:
    def say_good_morning(self):
        friend_name = input('Enter your friend name: ')
        print('Good morning ' + friend_name)


# Задача 2: Створіть клас Банк в якому буде декілька методів.
# exchange_rate_usd який буде виводити курс обміну гривні до доллара.exchange_rate_eur курс гривні до євро.
# card_expire_date - повідомлення до коли дійсна картка.
class Bank:
    def exchange_rate_usd(self):
        uha_to_usd = {'USD': 41.5}
        print(uha_to_usd['USD'])


# Задача 3: Створіть клас в якому буде метод, який буде викликати функцію(поза класом)
# яка буде питати в користувача число. і метод буде повертати це число в квадраті.
class Math:
    def pow_dialog(self):
        user_number = int(input('Enter number: '))
        result = user_number ** 2
        print(result)
