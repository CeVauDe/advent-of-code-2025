from copy import copy


def get_joiltage(bank: str, num_batteries: int = 12) -> int:
    assert len(bank) >= num_batteries
    highest_joltage = []
    for i, b in enumerate(bank):
        if len(highest_joltage) < num_batteries:
            highest_joltage += b
        else:
            max_start_index = max(0, len(highest_joltage) - (len(bank) - i))
            for j in range(max_start_index, len(highest_joltage)):
                trial_joltage = copy(highest_joltage)
                trial_joltage[j] = b
                if int("".join(trial_joltage)) > int("".join(highest_joltage)):
                    highest_joltage[j] = b
                    continue

    return int("".join(highest_joltage))


if __name__ == "__main__":
    with open("day3/input.txt", "r") as f:
        banks = f.readlines()
    banks = [b.strip() for b in banks]

    total_joltage = 0

    for bank in banks:
        total_joltage += get_joiltage(bank=bank)

    print(f"Total output joltage ist: {total_joltage}")
