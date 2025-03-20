# Задача 1: Запитайте в користувача два числа та поверніть йому суму цих чисел.
def task_1():
    num_1 = int(input("Введіть перше число:"))
    num_2 = int(input("Введіть друге число:"))

    print("Сумма двох чисел =", num_1 + num_2)

# Задача 2: Запитайте в користувача сторони прямокутника і за допомогою математичної формули та пайтона виведіть йому периметр та площу цього прямокутника.
def task_2():
    side_a = int(input("Enter length of rectangle:"))
    side_b = int(input("Enter height of rectangle:"))

    p = (side_a + side_b) * 2
    s = side_a * side_b

    print("Perimeter of rectangle is equal:", p)
    print("Area of rectangle is equal:", s)

# Задача 3 (з уроку): Зробіть задачу з уроку, але щоб знижка була у відсотках.
def task_3():
    print("welcome to discount counter!")
    payment = float(input("Enter price of item you want to buy:"))
    discount = float(input("Enter discount present:"))

    price = payment - ((payment/100) * discount)

    print("Final price is:", price)
