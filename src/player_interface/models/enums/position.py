from enum import Enum


class Position(Enum):
    ATTACK = "A"
    MIDFIELD = "M"
    DEFENSE = "D"
    GOALIE = "G"
    DEFENSIVE_Midfield = "DM"
    LONG_STICK_MIDFIELD = "LSM"

    def __str__(self) -> str:
        return str.capitalize(self.name)
