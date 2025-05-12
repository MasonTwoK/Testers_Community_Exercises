# Створіть фікстуру test_data зі області видимості function та переконайтеся, що кожен тест викликає фікстуру,
# яка виводить "test start" перед тестом і "test finish" після завершення тесту.
import pytest


@pytest.fixture(scope="function")
def test_data():
    print('test start')
    yield
    print('test finish')

