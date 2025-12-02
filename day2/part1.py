from typing import NamedTuple


class Range(NamedTuple):
    start: int
    stop: int


class IdChecker:
    def __init__(self):
        pass

    @staticmethod
    def validate_id(id_: int) -> bool:
        as_str = str(id_)
        length = len(as_str)

        if length % 2 != 0:
            return True

        half = length // 2
        # print(f"{as_str[:half]=} | {as_str[half:]=}")
        if as_str[:half] == as_str[half:]:
            return False

        return True

    @classmethod
    def get_invalid_ids(cls, id_range: Range) -> set[int]:
        invalid_ids = set()
        for i in range(id_range.start, id_range.stop + 1):
            if not cls.validate_id(i):
                invalid_ids.add(i)

        return invalid_ids

    @classmethod
    def get_invalid_ids_from_str(cls, range_str: str) -> set[int]:
        r = range_str.split("-")
        return cls.get_invalid_ids(Range(int(r[0]), int(r[1])))

    @classmethod
    def get_sum_from_line(cls, line: str) -> int:
        ranges = line.split(",")

        invalid_ids = set()
        for r_str in ranges:
            invalid_ids.update(cls.get_invalid_ids_from_str(r_str))

        return sum(invalid_ids)


if __name__ == "__main__":
    with open("day2/input.txt", "r") as f:
        input_line = f.readline()

    id_checker = IdChecker()
    invalid_id_sum = id_checker.get_sum_from_line(input_line)

    print(f"Sum of invalid ids:{invalid_id_sum}")
