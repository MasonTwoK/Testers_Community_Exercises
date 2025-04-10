# Задача 1: Створіть список grades зі значеннями оцінок (наприклад, 5, 3, 4, 2, 5).
# Видаліть всі низькі оцінки (менше або рівно 3) за допомогою циклу та відсортуйте. Виведіть оновлений список.
list_of_grades = [5, 3, 4, 2, 5]

iterator = 0
for grade in list_of_grades:
    if grade <= 3:
        list_of_grades.pop(iterator)
    iterator += 1

list_of_grades.sort()
print(list_of_grades)

# Задача 2: Створіть 2 списки з декількома різними словами.Об'єднайте їх за допомогою методу списку.
# Виведіть кожне слово, до кожного слова вказівник на його довжину (кількість символів) у форматі: "слово (довжина)".
# Використайте цикл for для цього.
list_of_fruits = ["cherry", "coconut", "apple", "avocado"]
list_of_veggies = ["potato", "cucumber", "tomato"]

combined_list = list_of_fruits.copy()
combined_list.extend(list_of_veggies)

for item in combined_list:
    print(f"{item} ({len(item)})")

# Задача 3: Створити список (наприклад такий ["apple", "grape", "kiwi", "pear", "melon", "banana", "mango"]).
# За допомогою методу із відео на уроці відсортуйте список за зростанням довжини слів та зробіть вивід на екран.
list_of_items = ["apple", "grape", "kiwi", "pear", "melon", "banana", "mango"]
list_of_items.sort(key=len)
print(list_of_items)


# **Додаткові завдання:**
# Задача 4:
my_list = [2, -100, 30, 15.5, 32]
# Напишіть програму яка буде сортувати вказаний вище список в залежності від того що введе користувач.
# Якщо він введе 'спад' то список повинний йти від більшого елемента до меншого.
# Якщо він введе 'виріст' то від меншого до більшого. Не забутьте що користувач може ввести в будь якому регістрі.
# Якщо ж він введе щось третє, то виведіть йому повідомлення 'некоректний ввід'
user_input = input("Введіть 'спад' або 'виріст': ")
if user_input.lower() == 'спад':
    result = my_list.sort(reverse=True)
    print(result)
elif user_input.lower() == 'виріст':
    result = my_list.sort()
    print(result)
else:
    print('некоректний ввід')
