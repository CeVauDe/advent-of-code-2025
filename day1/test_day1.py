import pytest

from day1 import NorthPoleSafe


@pytest.fixture
def safe() -> NorthPoleSafe:
    return NorthPoleSafe(initial_dial_pos=50)


class TestNorthPoleSafe:
    def test_init_safe(self) -> None:
        safe = NorthPoleSafe(initial_dial_pos=50)

        assert safe.dial_pos == 50

    def test_rotate_dial_left(self, safe) -> None:
        safe.dial("L10")

        assert safe.dial_pos == 40

    def test_rotate_dial_right(self, safe) -> None:
        safe.dial("R10")

        assert safe.dial_pos == 60

    def test_rotate_dial_left_overflow_once(self, safe) -> None:
        safe.dial("L68")

        assert safe.dial_pos == 82

    def test_rotate_dial_left_overflow_multiple(self, safe) -> None:
        safe.dial("L168")

        assert safe.dial_pos == 82

    def test_rotate_dial_right_overflow_once(self, safe) -> None:
        safe.dial("R68")

        assert safe.dial_pos == 18

    def test_rotate_dial_right_overflow_multiple(self, safe) -> None:
        safe.dial("R168")

        assert safe.dial_pos == 18

    def test_rotate_dial_reaches_100_eq_0(self, safe) -> None:
        safe.dial("R50")

        assert safe.dial_pos == 0

    def test_dial_sequence(self, safe) -> None:
        safe.dial_sequence(
            ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
        )

        assert safe.dial_pos == 32

    def test_count_0_positions(self, safe) -> None:
        safe.dial_sequence(
            ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
        )

        assert safe.num_0_positions == 3
