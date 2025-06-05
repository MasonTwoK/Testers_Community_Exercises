import pytest


# Задача 2: Створіть фікстуру numbers, яка повертає кортеж чисел (1, 2, 3, 4, 5).
@pytest.fixture
def numbers(tuple_5=(1, 2, 3, 4, 5)):
    yield tuple_5


class FixtureValues:
    def __init__(self, value_1, value_2):
        self.value_1 = value_1
        self.value_2 = value_2


@pytest.fixture
def db_connection_disconnection(fixture_values=FixtureValues(value_1=1, value_2=2)):
    print("db connected")
    yield fixture_values
    print("db disconnected")
