import pytest

from day3 import get_joiltage


@pytest.mark.parametrize("bank,joiltage", [("987", 98), ("876", 87), ("854", 85)])
def test_get_joiltage(bank: str, joiltage: int) -> None:
    assert get_joiltage(bank) == joiltage
