import pytest


@pytest.fixture
def database_interaction():
    print("db is connected")
    yield
    print("db is disconnected")
