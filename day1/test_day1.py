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

        assert safe.num_0_positions == 6

    def test_count_1000_clicks(self, safe) -> None:
        safe.dial("R1000")

        assert safe.num_0_positions == 10

    def test_count_dial_left_to_0(self, safe) -> None:
        safe.dial("L50")

        assert safe.num_0_positions == 1

    def test_count_dial_right_to_0(self, safe) -> None:
        safe.dial("R50")

        assert safe.num_0_positions == 1

    def test_count_dial_left_to_0_multiturn(self, safe) -> None:
        safe.dial("L150")
        assert safe.num_0_positions == 2

    def test_count_dial_right_to_0_multiturn(self, safe) -> None:
        safe.dial("R150")
        assert safe.num_0_positions == 2

    def test_count_dial_L68(self) -> None:
        safe = NorthPoleSafe(initial_dial_pos=50)
        safe.dial("L68")
        assert safe.num_0_positions == 1
        assert safe.dial_pos == 82

    def test_count_dial_L30(self) -> None:
        safe = NorthPoleSafe(initial_dial_pos=82)
        safe.dial("L30")
        assert safe.num_0_positions == 0
        assert safe.dial_pos == 52

    def test_count_dial_R48(self) -> None:
        safe = NorthPoleSafe(initial_dial_pos=52)
        safe.dial("R48")
        assert safe.num_0_positions == 1
        assert safe.dial_pos == 0

    def test_count_dial_L5(self) -> None:
        safe = NorthPoleSafe(initial_dial_pos=0)
        safe.dial("L5")
        assert safe.num_0_positions == 0
        assert safe.dial_pos == 95

    def test_count_dial_R60(self) -> None:
        safe = NorthPoleSafe(initial_dial_pos=95)
        safe.dial("R60")
        assert safe.num_0_positions == 1
        assert safe.dial_pos == 55

    def test_count_dial_L55(self) -> None:
        safe = NorthPoleSafe(initial_dial_pos=55)
        safe.dial("L55")
        assert safe.num_0_positions == 1
        assert safe.dial_pos == 0

    def test_count_dial_L1(self) -> None:
        safe = NorthPoleSafe(initial_dial_pos=0)
        safe.dial("L1")
        assert safe.num_0_positions == 0
        assert safe.dial_pos == 99

    def test_count_dial_L99(self) -> None:
        safe = NorthPoleSafe(initial_dial_pos=99)
        safe.dial("L99")
        assert safe.num_0_positions == 1
        assert safe.dial_pos == 0

    def test_count_dial_R14(self) -> None:
        safe = NorthPoleSafe(initial_dial_pos=0)
        safe.dial("R14")
        assert safe.num_0_positions == 0
        assert safe.dial_pos == 14

    def test_count_dial_L82(self) -> None:
        safe = NorthPoleSafe(initial_dial_pos=14)
        safe.dial("L82")
        assert safe.num_0_positions == 1
        assert safe.dial_pos == 32
