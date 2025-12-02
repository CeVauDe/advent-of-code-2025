from part1 import IdChecker


class TestIdChecker:
    def test_init_id_checker(self) -> None:
        id_checker = IdChecker()
        assert isinstance(id_checker, IdChecker)
