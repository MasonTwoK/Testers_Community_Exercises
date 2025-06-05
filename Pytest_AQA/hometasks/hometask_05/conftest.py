# Задача 1
# Створити фікстури для імітації отримання даних через API з різними скоупами.
# Потрібно створити фікстури під кожний з основних скоупів (function, class, module, package, session),
# які будуть повертати імітовані дані з АПІ.
# Напишіть тести, які запускаються тільки для двох скоупів: function і session.
import pytest


@pytest.fixture(scope="function")
def scope_function(api_data_function=11):
    print("setup for functional scope reached")
    yield api_data_function
    print("teardown for functional scope reached")


@pytest.fixture(scope="class")
def scope_class(api_data_class=12):
    print("setup for class scope reached")
    yield api_data_class
    print("teardown for class scope reached")


@pytest.fixture(scope="module")
def scope_module(api_data_module=13):
    print("setup for module scope reached")
    yield api_data_module
    print("teardown for module scope reached")


@pytest.fixture(scope="package")
def scope_package(api_data_package=14):
    print("setup for package scope reached")
    yield api_data_package
    print("teardown for package scope reached")


@pytest.fixture(scope="session")
def scope_session(api_data_session=15):
    print("setup for session scope reached")
    yield api_data_session
    print("teardown for session scope reached")


# Задача 2
# Створити фікстуру initial_data зі скоупом module, яка повертає список з  трьома іменами.
# Написати тест test_data_length, який перевіряє, напишіть два теста де ви використаєте цю фікстуру.
@pytest.fixture(scope="module")
def initial_data():
    names = ['Mark', 'Luke', 'John']
    yield names

