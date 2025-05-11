# Задача 1: Створити фікстури для імітації отримання даних через API з різними скоупами.
# Потрібно створити фікстури під кожний з основних скоупів (function, class, module, package, session),
# які будуть повертати імітовані дані з АПІ.
# Напишіть тести, які запускаються тільки для двох скоупів: function і session.
class TestSuiteHomeTask1:
    def test_hometask5_11(self, scope_function, scope_session):
        print("test hometask 5.1.1 running")
        assert True

    def test_hometask5_12(self, scope_function, scope_session):
        print("test hometask 5.1.2 running")
        assert False


# Задача 2: Створити фікстуру initial_data зі скоупом module, яка повертає список з  трьома іменами.
# Написати тест test_data_length, який перевіряє, напишіть два теста де ви використаєте цю фікстуру.
def test_data_length(initial_data):
    assert len(initial_data) == 3


def test_data_certain_name_contains(initial_data):
    assert 'Luke' in initial_data


# Задача 3: Перепишіть тест з попереднього уроку де в нас був Class TestA та містив setup_method
# та teardown_method зробіть три теста в середині цього класу.
# Та напишіть в коментарях до якого скоупу належить ваш setup_method та teardown_method.
# Якщо в вас є підписка на перевірку то вкажіть в здачі домашки скоуп.
# Відповідь: setup_method та teardown_method належать до functional scope
class TestClassA1:
    def setup_method(self):
        print('in class setup method reached')

    def teardown_method(self):
        print('in class teardown method reached')

    def test_func_a11(self, scope_session, scope_package, scope_module, scope_class, scope_function):
        print("test a.11 is running")
        assert True

    def test_func_a12(self, scope_session, scope_package, scope_module, scope_class, scope_function):
        print("test a.12 is running")
        assert True

    def test_func_a13(self, scope_session, scope_package, scope_module, scope_class, scope_function):
        print("test a.13 is running")
        assert True
