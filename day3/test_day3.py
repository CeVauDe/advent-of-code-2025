import pytest

from day3 import get_joiltage


@pytest.mark.parametrize(
    "bank,joiltage",
    [
        ("987", 98),
        ("876", 87),
        ("854", 85),
        ("757", 77),
        ("345", 45),
        ("811111111111119", 89),
        ("987654321111111", 98),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ],
)
def test_get_joiltage(bank: str, joiltage: int) -> None:
    assert get_joiltage(bank) == joiltage
