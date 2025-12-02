from typing import NamedTuple


class Range(NamedTuple):
    start: int
    stop: int


def validate_id(id_: int) -> bool:
    as_str = str(id_)
    length = len(as_str)

    for seq_len in range(1, length):
        chunks = {as_str[i : i + seq_len] for i in range(0, length, seq_len)}
        # print(chunks)
        if len(chunks) == 1:
            return False

    return True


def get_invalid_ids(id_range: Range) -> set[int]:
    invalid_ids = set()
    for i in range(id_range.start, id_range.stop + 1):
        if not validate_id(i):
            invalid_ids.add(i)

    return invalid_ids


def get_sum_from_line(line: str) -> int:
    ranges = line.split(",")

    invalid_ids = set()
    for r_str in ranges:
        r = r_str.split("-")
        invalid_ids.update(get_invalid_ids(Range(int(r[0]), int(r[1]))))

    return sum(invalid_ids)


if __name__ == "__main__":
    with open("day2/input.txt", "r") as f:
        input_line = f.readline()

    invalid_id_sum = get_sum_from_line(input_line)

    print(f"Sum of invalid ids: {invalid_id_sum}")
