import pytest


@pytest.mark.smoke
def test_1():
    assert True


@pytest.mark.regression
def test_2():
    assert True


@pytest.mark.retest
def test_3():
    assert True


@pytest.mark.smoke
def test_4():
    assert True


@pytest.mark.regression
def test_5():
    assert True


@pytest.mark.retest
def test_6():
    assert True


@pytest.mark.smoke
def test_7():
    assert True


@pytest.mark.regression
def test_8():
    assert True


@pytest.mark.retest
def test_9():
    assert True


@pytest.mark.smoke
def test_10():
    assert True
