from collections import Counter


def get_joiltage(bank: str, num_batteries: int = 12) -> int:
    assert len(bank) >= num_batteries

    counts = Counter(bank)

    for i in range(10, 0, -1):
        if counts.get(str(i), 0) >= num_batteries:
            return int(str(i) * num_batteries)

    highest_joltage = ""
    for b in bank:
        if len(highest_joltage) < num_batteries:
            highest_joltage += b

    return int(highest_joltage)


if __name__ == "__main__":
    with open("day3/input.txt", "r") as f:
        banks = f.readlines()
    banks = [b.strip() for b in banks]

    total_joltage = 0

    for bank in banks:
        total_joltage += get_joiltage(bank=bank)

    print(f"Total output joltage ist: {total_joltage}")
