import time
from time import sleep

class TestNew:
    def test_1(self):
        assert True

    def test_2(self):
        assert True


def test_3():
    assert True


def test_qa_2():
    assert True


def test_qa_3():
    assert False


def test_qa_4():
    assert False


def test_qa_5():
    time.sleep(2)
    assert True


def test_qa_6():
    time.sleep(1)
    assert True
