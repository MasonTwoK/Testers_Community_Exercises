import pytest


@pytest.mark.order(1)
def test_db_connection():
    print('db connected')
    assert True


@pytest.mark.order(3)
def test_db_disconnect():
    print('db disconnected')
    assert True


@pytest.mark.order(2)
def test_data_check():
    print('data check')
    assert True
