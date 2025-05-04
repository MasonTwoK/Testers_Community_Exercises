# Задача 1
# Написати цикл for,
# який обраховує суму всіх чисел у списку numbers = [1, 2, 3, 4, 5].
nums_list = [1,2,3,4,5]
nums_sum = 0

for iterator in nums_list:
    nums_sum += iterator

print(f"Values in list: {nums_list}")
print(f"Sum of all numbers in list: {nums_sum}")


# Задача 2
# Використовуючи цикл for,
# напишіть код, який ітерує по списку numbers = [-2, -1, 0, 1, 2] і виводить тільки позитивні числа.
nums_list = [-2, -1, 0, 1, 2]

for iterator in nums_list:
    if iterator > 0:
        print(iterator)


# Задача 3
# Використовуючи цикл for,
# створіть новий список, що містить квадрати всіх чисел у вихідному списку numbers = [1, 2, 3, 4, 5].
nums_list = [1, 2, 3, 4, 5]
pows_list = []

for iterator in nums_list:
    pows_list.append(iterator * iterator)

print(f"List with nums: {nums_list}")
print(f"List with pows: {pows_list}")

# Задача 4: Напишіть програму яка проходить по списку з словами та виводить кількість букв у кожному слові.
# і якщо слово більше десяти букв то виводить повідомлення "Ого яке довге слово"
# якщо слово менше 4 букв то виводить повідомлення "Ого яке коротке слово".
list_of_word = ['cat', 'dog', 'bird', 'snake', 'hippokapibara']

for word in list_of_word:
    word_size = len(word)
    print(word_size)
    if word_size > 10:
        print("Ого яке довге слово")
    if word_size < 4:
        print("Ого яке коротке слово")
