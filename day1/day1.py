class NorthPoleSafe:
    def __init__(self, initial_dial_pos: int):
        self.dial_pos = initial_dial_pos
        self.NUM_DIAL_POSITIONS = 100
        self._MIN_POS = 0
        self._MAX_POS = self.NUM_DIAL_POSITIONS - self._MIN_POS - 1
        self.num_0_positions = 0

    def dial(self, rotation: str) -> None:
        dir = rotation[0]
        distance = int(rotation[1:])

        assert dir in ["L", "R"]

        sign = -1 if dir == "L" else 1

        update_pos_by = distance % self.NUM_DIAL_POSITIONS
        turns = abs(distance // self.NUM_DIAL_POSITIONS)

        self.num_0_positions += turns

        new_pos = self.dial_pos + update_pos_by * sign

        if new_pos <= self._MIN_POS or new_pos > self._MAX_POS:
            if self.dial_pos != 0:
                self.num_0_positions += 1
            new_pos %= self.NUM_DIAL_POSITIONS

        print(
            f"old: {self.dial_pos:2d} | new: {new_pos:2d} | dialed: {rotation:>4} | total 0s: {self.num_0_positions} | turns: {turns}"
        )
        self.dial_pos = new_pos

    def dial_sequence(self, sequence: list[str]) -> None:
        for rotation in sequence:
            self.dial(rotation=rotation)


if __name__ == "__main__":
    with open("day1/input.txt", "r") as f:
        sequence = f.readlines()

    print(f"Sequence has {len(sequence)} items")

    safe = NorthPoleSafe(initial_dial_pos=50)
    safe.dial_sequence(sequence)

    print(f"Password is: {safe.num_0_positions}")
