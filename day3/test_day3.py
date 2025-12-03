from day3 import get_joiltage


def test_get_joiltage() -> None:
    j = get_joiltage("987")

    assert j == 98
