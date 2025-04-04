# Задача 1: Запитайте в користувача два числа та поверніть йому суму цих чисел.
num_1 = int(input("Введіть перше число:"))
num_2 = int(input("Введіть друге число:"))

result = num_1 + num_2
print(result)

# Задача 2: Запитайте в користувача сторони прямокутника і
# за допомогою математичної формули та пайтона виведіть йому периметр та площу цього прямокутника.
side_a = int(input("Enter length of rectangle:"))
side_b = int(input("Enter height of rectangle:"))

perimeter = (side_a + side_b) * 2
area = side_a * side_b

print("Perimeter of rectangle is equal:", perimeter)
print("Area of rectangle is equal:", area)

# Задача 3 (з уроку): Зробіть задачу з уроку, але щоб знижка була у відсотках.
print("welcome to discount counter!")
payment = float(input("Enter price of item you want to buy:"))
discount = float(input("Enter discount present:"))

price = payment - ((payment/100) * discount)

print("Final price is:", price)

# Задача 4: Запитайте в користувач рік його народження.
# І рік в якому він хоче знати свій вік і виведіть йому три окремих результати:
# 1) Скільки йому буде років.
# 2) Скільки йому буде днів
# 3) Скільки йому буде годин
# Округлюйте результат до більшого значення.
# Тобто нам не важливо що користувач народився 2001 році в грудні ми рахуємо що в 2001 він прожив 1 рік,
# 12 місяців та 365 днів.
year_of_birth = int(input("Введіть свій рік народжння: "))
year_to_know = int(input("Введіть рік в якому ви хочете знати свій вік: "))

result = (year_to_know - year_of_birth+1)
print(result)

result = (year_to_know - year_of_birth+1) * 365
print(result)

result = (year_to_know - year_of_birth+1) * 365 * 24
print(result)
