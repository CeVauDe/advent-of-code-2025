def get_joiltage(bank: str, num_batteries: int = 12) -> int:
    assert len(bank) >= num_batteries
    joltage = []

    for i, b in enumerate(reversed(bank)):
        joltage += b

    return int("".join(reversed(joltage)))


if __name__ == "__main__":
    with open("day3/input.txt", "r") as f:
        banks = f.readlines()
    banks = [b.strip() for b in banks]

    total_joltage = 0

    for bank in banks:
        joilage = get_joiltage(bank=bank)
        print(f" | Output joltage ist: {joilage}")
        total_joltage += joilage

    print(f"Total output joltage ist: {total_joltage}")
