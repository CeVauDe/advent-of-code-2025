from typing import NamedTuple


class Range(NamedTuple):
    start: int
    stop: int


class IdChecker:
    def __init__(self):
        self.sum = 0

    def validate_id(self, id_: int) -> None:
        as_str = str(id_)
        length = len(as_str)

        if length % 2 != 0:
            return

        half = length // 2
        if as_str[:half] == as_str[half:]:
            print(f"invalid id: {id_:10d} | new sum: {self.sum}")
            self.sum += id_

    def check_invalid_ids(self, id_range: Range):
        for i in range(id_range.start, id_range.stop + 1):
            self.validate_id(i)

    def get_invalid_ids_from_str(self, range_str: str) -> set[int]:
        r = range_str.split("-")
        self.check_invalid_ids(Range(int(r[0]), int(r[1])))

    def get_sum_from_line(self, line: str) -> int:
        ranges = line.split(",")

        for r_str in ranges:
            self.get_invalid_ids_from_str(r_str)

        return self.sum


if __name__ == "__main__":
    with open("day2/input.txt", "r") as f:
        input_line = f.readline()

    id_checker = IdChecker()
    invalid_id_sum = id_checker.get_sum_from_line(input_line)

    print(f"Sum of invalid ids: {invalid_id_sum}")
