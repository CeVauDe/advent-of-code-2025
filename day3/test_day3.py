from day3 import get_joiltage


def test_get_joiltage() -> None:
    j = get_joiltage("987")

    assert j == 98


def test_get_joiltage_2() -> None:
    assert get_joiltage("876") == 87


def test_get_joiltage_3() -> None:
    assert get_joiltage("854") == 85
