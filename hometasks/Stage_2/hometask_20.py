# Задача 1: Створіть файл, в якому будуть дві функції: для множення чисел та ділення.
# Імпортуйте ці функції у файл main.py та використайте їх для обчислення результатів для чисел 10 та 2.


# Задача 2: Створіть файл, де визначіть функцію, яка обчислює площу прямокутника.
# Потім імпортуйте цю функцію у файл main.py та використайте для обчислення площі прямокутника зі сторонами 4 та 6.

# Задача 3: Напишіть функції які конвертують вагу з кілограмів у фунти та навпаки.
# Параметр за замовчуванням для обох функцій повинен бути 100.
# Після цього імпортуйте ці функції у файл main.py
# та скористайтеся ними для конвертації ваги 42 кг у фунти та 89 фунтів у кілограми.
# Зробіть вивід результату конвертації на екран.
def weight_converter_kg_to_lb(weight_in_kg=100):
    lb = weight_in_kg * 0.453592
    return lb


def weight_converter_lb_to_kg(weight_in_lb=100):
    kg = weight_in_lb * 2.20462
    return kg


weight_converter_kg_to_lb(weight_in_kg=42)
weight_converter_lb_to_kg(weight_in_lb=89)
