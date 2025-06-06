# Задача 1: Напишіть клас для тестування бази даних як на уроці з відео,
# де використовується методи "setup" та "teardown" для підключення і відключення від бази даних.
# Та зробіть декілька тестів для перевірки якогось значення заданого у "setup".


class TestSuiteIntegrationBD:
    def setup_method(self):
        print("DB is connected")
        self.data = 1

    @staticmethod
    def teardown_method(self):
        print("DB is disconnected")

    def test_qa_1(self):
        print("test db 1 run")
        assert self.data == 1

    def test_qa_2(self):
        print("test db 2 run")
        assert self.data == 2


# Задача 2: Створіть фікстуру numbers, яка повертає кортеж чисел (1, 2, 3, 4, 5).
# Використайте цю фікстуру у двох тестах для перевірки суми чисел у кортежі та перевірки наявності числа.
# Напишіть фікстуру numbers, яка повертає кортеж чисел.
# Напишіть тест test_addition, щоб перевірити, чи сума чисел у кортежі дорівнює 15.
# Напишіть тест test_found, щоб перевірити, чи число 5 є у кортежі

def test_addition(numbers):
    assert sum(numbers) == 15


def test_found(numbers):
    assert 5 in numbers


# Задача 3: Створіть набір тестів,
# які використовують одну фікстуру для підготовки даних перед кожним тестом та очищення після нього.
def test_qa_3(db_connection_disconnection):
    assert 1 == db_connection_disconnection.value_1


def test_qa_4(db_connection_disconnection):
    assert 0 == db_connection_disconnection.value_2
