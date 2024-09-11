from dataclasses import dataclass


@dataclass
class Player:
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


@dataclass
class Lineup:
    start_player = Player()
    players_list: list

    @property
    def count(self):
        return len(self.players_list)

    def add_player(self, start_player: Player):
        start_player.f_name = str(input("Enter player first name: "))
        start_player.l_name = str(input("Enter player last name: "))
        start_player.position = str(input("Enter player position: "))
        start_player.at_bats = int(input("enter player times at bats: "))
        start_player.hits = int(input("enter player hits: "))
        self.players_list.append(start_player)
        print(f"Player {start_player.full_name} was add to the lineup")

    def remove_player(self, player_list: list):
        player_number = int(input("Enter player number: "))
        removed_player = player_list.pop(player_number - 1)
        print(f"Player {removed_player.full_name} was removed from lineup")

    def move_player(self, player_list: list):
        player_number = int(input("Enter player number: "))
        popped_player = player_list.pop(player_number - 1)
        new_list_place = int(input("Enter new player number: "))
        self.players_list[new_list_place].insert(popped_player)
        print(f"Player {popped_player.full_name} was moved in the lineup")

    def edit_player(self, player_list: list):
        player_number = int(input("Enter player number: "))

    def __iter__(self):
        for player in self.player_list:
            yield player

