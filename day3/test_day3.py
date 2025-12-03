import pytest

from day3 import get_joiltage


@pytest.mark.parametrize(
    "bank,joiltage",
    [
        ("999999999999", 999999999999),
        ("987654321111111", 987654321111),
        ("811111111111119", 811111111119),
        ("234234234234278", 434234234278),
        ("818181911112111", 888911112111),
    ],
)
def test_get_joiltage(bank: str, joiltage: int) -> None:
    assert get_joiltage(bank) == joiltage


@pytest.mark.parametrize(
    "bank,joiltage",
    [
        ("999", 999),
        ("42434", 444),
        ("432", 432),
        ("4323", 433),
        ("2342", 342),
    ],
)
def test_get_joilage_3_batteries(bank: str, joiltage: int) -> None:
    assert get_joiltage(bank, num_batteries=3) == joiltage
