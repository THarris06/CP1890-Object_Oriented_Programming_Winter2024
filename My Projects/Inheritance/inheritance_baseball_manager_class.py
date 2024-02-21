from dataclasses import dataclass


@dataclass
class Player:
    first_name: str = ''
    last_name: str = ''
    position: str = ''
    atbats: int = 0
    hits: int = 0

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def get_average(self):
        try:
            avg = self.hits / self.atbats
            return avg
        except ZeroDivisionError:
            return 0.0


def main():
    player1 = Player('Arun', 'Rameshbabu', 'S', 10, 10)
    print(f'Player: {player1.full_name}')
    print(f'Batting Average: {player1.get_average}')
    print('Test complete')


if __name__ == '__main__':
    main()
