# Задача 1:
# Зробіть кілька тестів як ми це робили на уроці,
# та за допомогою командного рядка запустіть тести у два потоки використовуючи інформативний вивід.
# Рішення: pytest <..\Testers_Community_Exercises\Pytest_AQA\hometasks\hometask_08\hometask_08_test.py> -v -n 2
import time


def test_1():
    """Basic truth test."""
    assert True


def test_2():
    """Check if 5 is greater than 3."""
    assert 5 > 3


def test_3():
    """Verify an empty list evaluates to False."""
    assert not []


def test_4():
    """Ensure 'Python' is a string."""
    assert isinstance("Python", str)


def test_5():
    """Check if None is falsy."""
    assert not None


def test_6():
    """Ensure a positive number is greater than zero."""
    assert 10 > 0


def test_7():
    """Verify a tuple is immutable."""
    assert isinstance((1, 2, 3), tuple)


def test_8():
    """Ensure 'hello' starts with 'h'."""
    assert "hello".startswith("h")


def test_9():
    """Confirm a set eliminates duplicates."""
    assert len({1, 1, 2, 2, 3}) == 3


def test_10():
    """Check if an empty dictionary evaluates to False."""
    assert not {}


# Задача 2:
# Скопіюйте тести які ми створювали на 6 уроці або створіть нові та додайте кожному тесту 2 секунди затримки
# використовуючи бібліотеку time. Та запустіть тести у пяти потоках.
# Рішення: pytest <..\Testers_Community_Exercises\Pytest_AQA\hometasks\hometask_08\hometask_08_test.py::TestTask2> -n 5

class TestTask2:
    def test_11(self):
        """Check if a list contains a specific element."""
        time.sleep(2)
        assert 3 in [1, 2, 3, 4, 5]

    def test_12(self):
        """Ensure string concatenation works correctly."""
        time.sleep(2)
        assert "Hello" + " " + "World" == "Hello World"

    def test_13(self):
        """Verify division results in a float."""
        time.sleep(2)
        assert isinstance(10 / 2, float)

    def test_14(self):
        """Confirm a dictionary has a specific key."""
        time.sleep(2)
        assert "name" in {"name": "Alice", "age": 25}

    def test_15(self):
        """Ensure a negative number is less than zero."""
        time.sleep(2)
        assert -5 < 0

    def test_16(self):
        """Check if reversing a list works."""
        time.sleep(2)
        assert list(reversed([1, 2, 3])) == [3, 2, 1]


# Задача 3:
# Зробіть запуски першої та  другої задачі  використовуючи автотоматичну кількість потоків.
# Рішення: pytest <..\Testers_Community_Exercises\Pytest_AQA\hometasks\hometask_08\hometask_08_test.py> -n auto
