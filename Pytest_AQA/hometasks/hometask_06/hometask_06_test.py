# Задача 1: Напишіть три тестові функції: test_first(), test_second(), test_third().
# Використайте декоратори або для встановлення порядку виконання цих тестів.
# Наприклад, переконайтеся, що test_first() виконується перед test_second(), а test_second() - перед test_third().
import pytest


@pytest.mark.order(after="test_qa_1")
def test_first():
    assert True


@pytest.mark.order(after="test_first")
def test_second():
    assert True


@pytest.mark.order(after="test_second")
def test_third():
    assert True


# Задача 2: Створіть тести, де результат виконання одного тесту впливає на наступний.
# Наприклад, переконайтеся, що після успішного виконання test_login() виконується test_access_granted(),
# а після невдалого виконання test_login() - test_access_denied()
# @pytest.mark.skip(reason="task solution is wrong")
def test_login(result=True):
    assert result


@pytest.mark.order()
def test_access_granted():
    assert True


@pytest.mark.order(after='denied')
def test_access_denied():
    assert True


# Задача 3: Створіть 10 тестів  (можно взяти з другого уроку)  промаркуйте порядок виконання від 1 до 10.
# Створіть фікстуру test_data зі області видимості function та переконайтеся, що кожен тест викликає фікстуру,
# яка виводить "test start" перед тестом і "test finish" після завершення тесту.
# Підтвердіть, що тести виконуються у вірному порядку відповідно до маркерів,
# а також виводять необхідні повідомлення фікстури.
@pytest.mark.order(1)
def test_qa_10(test_data):
    assert True


@pytest.mark.order(2)
def test_qa_9(test_data):
    assert True


@pytest.mark.order(3)
def test_qa_8(test_data):
    assert True


@pytest.mark.order(4)
def test_qa_7(test_data):
    assert True


@pytest.mark.order(5)
def test_qa_6(test_data):
    assert True


@pytest.mark.order(6)
def test_qa_5(test_data):
    assert True


@pytest.mark.order(7)
def test_qa_4(test_data):
    assert True


@pytest.mark.order(8)
def test_qa_3(test_data):
    assert True


@pytest.mark.order(9)
def test_qa_2(test_data):
    assert True


@pytest.mark.order(10)
def test_qa_1(test_data):
    assert True
