import pytest

from day3 import get_joltage, get_num_higher_digits_left


@pytest.mark.parametrize(
    "digit,bank,expectation",
    [(3, "456", 3), (8, "136542642844", 0)],
)
def test_get_num_higher_digits_left(digit: int, bank: str, expectation: int) -> None:
    assert get_num_higher_digits_left(digit, bank) == expectation


@pytest.mark.parametrize(
    "bank,joltage",
    [
        ("999999999999", 999999999999),
        ("987654321111111", 987654321111),
        ("811111111111119", 811111111119),
        ("234234234234278", 434234234278),
        ("818181911112111", 888911112111),
        (
            "4732321333332463233337712234322122322247222252423773321362313613333336333732233372323328332333322777",
            833333322777,
        ),
    ],
)
def test_get_joiltage(bank: str, joltage: int) -> None:
    assert get_joltage(bank) == joltage


@pytest.mark.parametrize(
    "bank,joltage",
    [
        ("999", 999),
        ("42434", 444),
        ("432", 432),
        ("4323", 433),
        ("2342", 342),
    ],
)
def test_get_joilage_3_batteries(bank: str, joltage: int) -> None:
    assert get_joltage(bank, num_batteries=3) == joltage
