def enough_batteries_remaining_after_next_highest(
    battery_joltage: str, bank: str, min_remaining_length: int
) -> bool:
    for i, b in enumerate(bank):
        if b > battery_joltage and len(bank) - i >= min_remaining_length:
            return True
    return False


def make_largest_joltage(bank: str, num_batteries: int = 12) -> int:
    bank_joltage = ""

    for i, joltage in enumerate(bank):
        num_missing = num_batteries - len(bank_joltage)

        if enough_batteries_remaining_after_next_highest(
            joltage, bank[i:], num_missing
        ):
            continue

        elif num_missing <= 0:
            break

        bank_joltage += joltage

    return int(bank_joltage)


if __name__ == "__main__":
    with open("day3/input.txt", "r") as f:
        banks = f.readlines()

    output_joltages = [make_largest_joltage(bank.strip()) for bank in banks]

    print(f"Total output joltage is: {sum(output_joltages)}")
