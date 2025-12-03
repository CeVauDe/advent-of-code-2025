def get_joiltage(bank: str) -> int:
    highest_battery = 0
    next_highest = 0
    for b in bank:
        if (j := int(b)) > highest_battery:
            highest_battery = j
            next_highest = 0
            continue
        elif (j := int(b)) > next_highest:
            next_highest = j

    return highest_battery * 10 + next_highest
