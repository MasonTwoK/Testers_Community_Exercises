import pytest
from calculator import addition


@pytest.mark.parametrize('first_number, second_number, result', (
    pytest.param(2, 3, 5, id='positive numbers'),
    pytest.param(-3, 6, 3, id='negative & positive numbers'),
    pytest.param(4.5, 3.3, 7.8, id='float numbers')
))
def test_calculator(first_number, second_number, result):
    assert addition(first_number=first_number, second_number=second_number) == result
