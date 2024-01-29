from dataclasses import dataclass


@dataclass
class player:
    f_name: str = ""
    l_name: str = ""
    position: str = ""
    at_bats: int = 0
    hits: int = 0

    @property
    def full_name(self):
        return f'{self.f_name} {self.l_name}'

    @property
    def bat_average(self) -> float:
        try:
            avg = self.hits / self.at_bats
            return avg
        except ZeroDivisionError:
            return 0.0



