from collections import Counter


def get_num_higher_digits_left(digit: int, bank: str) -> int:
    digits_left = Counter(bank)
    num_digits_left = 0
    for i in range(digit + 1, 10):
        num_digits_left += digits_left.get(str(i), 0)
    return num_digits_left


def get_num_same_digits_left(digit: int, bank: str) -> int:
    return Counter(bank).get(str(digit), 0)


def next_higher_digit_bank_still_long_enough(
    digit: int, bank: str, expected_remaining_length: int
) -> bool:
    for i, b in enumerate(bank):
        if digit < int(b):
            if len(bank) - i < expected_remaining_length:
                return False
            else:
                return True
    return False


def get_joltage(bank: str, num_batteries: int = 12) -> int:
    assert len(bank) >= num_batteries
    joltage = []

    for i, b in enumerate(bank):
        num_higher_joltage_batteries = get_num_higher_digits_left(int(b), bank[i + 1 :])

        num_missing_batteries = num_batteries - len(joltage)
        num_remaining_batteries = len(bank) - i

        # enough higher joltage batteries left to fill
        if num_missing_batteries < num_higher_joltage_batteries:
            continue

        # barely enough batteries remaining to fill missing
        elif num_missing_batteries >= num_remaining_batteries:
            joltage += bank[i:]
            break

        # enough same or higher joltage batteries left, so we not need to fill current slot
        elif next_higher_digit_bank_still_long_enough(
            int(b), bank[i:], num_missing_batteries
        ):
            continue

        elif num_missing_batteries <= 0:
            break

        joltage += b

    return int("".join(joltage))


if __name__ == "__main__":
    with open("day3/input.txt", "r") as f:
        banks = f.readlines()
    banks = [b.strip() for b in banks]

    total_joltage = 0

    for bank in banks:
        joltage = get_joltage(bank=bank)
        total_joltage += joltage

    print(f"Total output joltage ist: {total_joltage}")
