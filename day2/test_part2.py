import pytest
from part2 import Range, get_invalid_ids, get_sum_from_line, validate_id


@pytest.fixture
def line() -> str:
    return (
        "11-22,95-115,998-1012,1188511880-1188511890,"
        "222220-222224,1698522-1698528,446443-446449,38593856-38593862,"
        "565653-565659,824824821-824824827,2121212118-2121212124"
    )


@pytest.mark.parametrize(
    "id_", [11, 22, 99, 111, 1010, 1188511885, 222222, 38593859, 446446]
)
def test_validate_id_false(id_) -> None:
    assert not validate_id(id_)


@pytest.mark.parametrize("id_", [123, 12345])
def test_validate_id_true(id_) -> None:
    assert validate_id(id_)


@pytest.mark.parametrize(
    "id_range,invalid_ids",
    [
        (Range(11, 22), {11, 22}),
        (Range(95, 115), {99, 111}),
        (Range(998, 1012), {999, 1010}),
    ],
)
def test_get_invalid_ids(id_range: Range, invalid_ids: set[int]) -> None:
    assert get_invalid_ids(id_range) == invalid_ids


def test_get_sum_from_line(line) -> None:
    invalid_id_sum = get_sum_from_line(line)
    assert invalid_id_sum == 4174379265
