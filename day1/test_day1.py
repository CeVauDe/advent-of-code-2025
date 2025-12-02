import pytest

from day1 import NorthPoleSafe


@pytest.fixture
def safe() -> NorthPoleSafe:
    return NorthPoleSafe(initial_dial_position=50)


class TestNorthPoleSafe:
    def test_init_safe(self) -> None:
        safe = NorthPoleSafe(initial_dial_position=50)

        assert safe.dial_position == 50

    def test_rotate_dial_left(self, safe) -> None:
        safe.dial("L10")

        assert safe.dial_position == 40

    def test_rotate_dial_right(self, safe) -> None:
        safe.dial("R10")

        assert safe.dial_position == 60
