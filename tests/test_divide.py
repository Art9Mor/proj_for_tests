from src.divide import divide


def test_divide():
    assert divide(1_000_000, 2) == 500_000
    assert divide(10, 5) == 2
    assert divide(6.6, 2) == 3.3


def test_divide__division_zero():
    ...
