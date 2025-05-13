# Задача 1: Створіть функцію add_numbers(a, b, с) для додавання трьох чисел.
# Параметризуйте цю функцію для тестування з використанням pytest.param для таких випадків:
# -Додавання позитивних цілих чисел
# -Додавання від'ємного та позитивного числа
# -Додавання чисел з плавучою комою
import pytest
from Pytest_AQA.lessons.lesson_07.calculator import add_numbers, power, sum_list


@pytest.mark.parametrize('a, b, c, result', (
    (1, 2, 3, 6),
    (5, -3, 2, 4),
    (7.7, 0, 3.1, 10.8)
))
def test_add_numbers(a, b, c, result):
    assert add_numbers(a=a, b=b, c=c) == result


# Задача 2: Напишіть функцію піднесення до степіння та протестуйте її використовуючи 5 тестових наборів.
@pytest.mark.parametrize('number, base, result', (
    (2, 2, 4),
    (3, 3, 27),
    (8, 0, 1),
    (-3, 2, 9),
    ('2', '2', '4'),
    (0, 2, 0),

))
def test_power(number, base, result):
    assert power(number=number, base=base) == result


# Задача 3: Напишіть функцію sum_list(numbers), яка обчислює суму елементів списку numbers.
# Параметризуйте тести для цієї функції з використанням pytest.param для різних списків чисел, включаючи пустий список.
@pytest.mark.parametrize('list_of_data, result', (
    pytest.param([1, 2, 3], 6, id='Sum of integer numbers'),
    pytest.param([3.0, 0.5, 1.1], 4.6, id='Sum of float numbers'),
    pytest.param([], 0, id='Sum empty list'),
))
def test_sum_list(list_of_data, result):
    assert sum_list(list_of_data) == result
