# Задача 1:
# Користувач дає вам список (тобто в програмі у вас буде змінна зі списком оцінок), наприклад:
# class_marks = [11, 10, 11, 10, 8]
# Вам потрібно вирахувати середню оцінку в групі.
def task_1():
    list_of_marks = []

    mark_1 = int(input("Enter mark of student 1: "))
    list_of_marks.append(mark_1)

    mark_2 = int(input("Enter mark of student 2: "))
    list_of_marks.append(mark_2)

    mark_3 = int(input("Enter mark of student 3: "))
    list_of_marks.append(mark_3)

    avg_mark = sum(list_of_marks) / 3
    print(f"Average mark of group is: {avg_mark}")


# Задача 2:
# Попросіть користувача ввести рядок з 4 словами, збережіть це у список, видаліть два останні елементи.
# І додайте в кінець один елемент з вашим іменем.
def task_2():
    words_string = input("Enter 5 random names:")
    words_list = words_string.split(" ")
    words_list.pop()
    print("Pop called() Removed last name in list")
    words_list.pop()
    print("Pop called() Removed last name in list")

    words_list.append("Will")
    print("Added new name to list")

    print(f"Names list contains: {words_list}")
# Задача 3:
# Попросіть користувача ввести рядок зі словами, підрахуйте кількість цих слів і виведіть користувачу,
# скільки слів він ввів.
def task_3():
    words_string = input("Enter words: ")
    words_list = words_string.split(" ")

    print(f"Amount of entered words: {len(words_list)}")