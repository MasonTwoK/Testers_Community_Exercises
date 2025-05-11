import pytest


@pytest.fixture
def numbers(tuple_5=(1, 2, 3, 4, 5)):
    print("fixture setup reached")
    yield tuple_5
    print("fixture teardown reached")
