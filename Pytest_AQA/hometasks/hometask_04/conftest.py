import pytest


@pytest.fixture
def numbers(tuple_5=(1, 2, 3, 4, 5)):
    yield tuple_5


@pytest.fixture
def db_connection_disconnection():
    print("db connected")
    yield
    print("db disconnected")
