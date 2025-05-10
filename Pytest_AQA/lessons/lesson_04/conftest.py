import pytest


@pytest.fixture  # розібратись як працює фікстура
def database():
    print("connect db")
    data = 10
    yield data  # розібратись куди передаються дані у цьому рядку
    print("disconnect db")
