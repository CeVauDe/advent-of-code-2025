from day1 import NorthPoleSafe


class TestNorthPoleSafe:
    def test_init_safe(self) -> None:
        safe = NorthPoleSafe(initial_dial_position=50)

        assert safe.dial_position == 50
