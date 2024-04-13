import datetime


class Player:
    def __init__(self, **kwargs):
        self.__player_id = kwargs["playerid"]
        self.__number = kwargs["number"]
        self.__first_name = kwargs["first_name"]
        self.__last_name = kwargs["last_name"]
        self.__position = kwargs["position"]
        self.__grade = kwargs["grade"]
        self.__school = kwargs["school"]
        self.__created = kwargs["created"] | None
        self.__modified = kwargs["modified"] | None

    @property
    def player_id(self) -> str:
        return self.__player_id

    @property
    def number(self) -> int:
        return self.__number

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def position(self) -> str:
        return self.__position

    @property
    def grade(self) -> str:
        return self.__grade

    @property
    def school(self) -> str:
        return self.__school

    @property
    def created(self) -> datetime:
        return self.__created

    @property
    def modified(self) -> datetime:
        return self.__modified

    def __str__(self) -> str:
        return f"{self.number}. {self.last_name}, {self.first_name} [{self.position}] | {self.grade} at {self.school}"

    def to_dict(self) -> str:
        return {
            "player_id": f"{self.__player_id}",
            "number": f"{self.__number}",
            "first_name": f"{self.__first_name}",
            "last_name": f"{self.__last_name}",
            "position": f"{self.__position}",
            "grade": f"{self.__grade}",
            "school": f"{self.__school}",
            "create_date": f"{self.__created}",
            "modified_data": f"{self.__modified}",
        }