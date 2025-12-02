class NorthPoleSafe:
    def __init__(self, initial_dial_position: int):
        self.dial_position = initial_dial_position

    def dial(self, rotation: str) -> None:
        dir = rotation[0]
        distance = int(rotation[1:])

        assert dir in ["L", "R"]

        if dir == "L":
            self.dial_position -= distance
