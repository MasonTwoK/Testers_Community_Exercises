# Задача 1:
# Користувач дає вам список (тобто в програмі у вас буде змінна зі списком оцінок), наприклад:
# class_marks = [11, 10, 11, 10, 8]
# Вам потрібно вирахувати середню оцінку в групі.
class_marks = [11, 10, 11, 10, 8]

avg_mark = sum(class_marks) / len(class_marks)
print(f"Average mark of group is: {avg_mark}")


# Задача 2:
# Попросіть користувача ввести рядок з 4 словами, збережіть це у список, видаліть два останні елементи.
# І додайте в кінець один елемент з вашим іменем.
words_string = input("Enter 4 random names: ")
words_list = words_string.split(" ")
words_list.pop()
print("Pop called() Removed last name in list")
words_list.pop()
print("Pop called() Removed last name in list")

words_list.append("Will")
print("Added new name to list")

print(words_list)


# Задача 3:
# Попросіть користувача ввести рядок зі словами, підрахуйте кількість цих слів і виведіть користувачу,
# скільки слів він ввів.
words_string = input("Enter words: ")
words_list = words_string.split(" ")

result = len(words_list)
print(f"Amount of entered words: {result}")