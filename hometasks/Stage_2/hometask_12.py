# Задача 1: Створіть список grades зі значеннями оцінок (наприклад, 5, 3, 4, 2, 5).
# Видаліть всі низькі оцінки (менше або рівно 3) за допомогою циклу та відсортуйте. Виведіть оновлений список.
def task_1():
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
def task_2():
    list_of_fruits = ["cherry", "coconut", "apple", "avocado"]
    list_of_veggies = ["potato", "cucumber", "tomato"]

    combined_list = list_of_fruits.copy()
    combined_list.extend(list_of_veggies)

    for item in combined_list:
        print(f"{item} ({len(item)})")

# Задача 3: Створити список (наприклад такий ["apple", "grape", "kiwi", "pear", "melon", "banana", "mango"]).
# За допомогою методу із відео на уроці відсортуйте список за зростанням довжини слів та зробіть вивід на екран.
def task_3():
    list_of_items = ["apple", "grape", "kiwi", "pear", "melon", "banana", "mango"]
    list_of_items.sort(key=len)
    print(list_of_items)
