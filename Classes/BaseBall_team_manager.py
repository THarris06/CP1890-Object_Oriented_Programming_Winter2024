from datetime import datetime
from Ball_team_classes import player

POSITIONS = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')


def div_line():
    print("="*90)


def top_menu():
    print(f"{'BaseBall Team Manager':>50}")

    cur_date = datetime.now().date()
    print(f"\nCURRENT DATE:\t {cur_date}")
    game_date = datetime.fromisoformat(input('GAME DATE:\t\t ')).date()
    until_game = (game_date - cur_date).days
    print(f"DAYS UNTIL GAME: {until_game}")

    print()
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program\n")
    print("Positions")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")


def display_lineup(players):
    if players == None:
        print("No players")
    else:
        print(f"{'':3}{'player':40}{'POS':6}{'AB':>6}{'H':>6}{'AVG':>8}")
        print('-'* 90)
        for i, player in enumerate(players):
            print(f"{i:>3d}{player.full_name:40}{player.position:6}{player.at_bats:6d}{player.at_hits:6d}{player.bat_average}")


def add_player():
    first_name = input('FIRST NAME: ').title()
    last_name = input('LAST NAME: ').title()
    position = get_player_position()
    at_bats = get_at_bats()
    hits = get_hits()

    new_player = player(first_name, last_name, position, at_bats, hits)
    players.append(new_player)
    print(f"Player {player.full_name} was added. \n")


def get_player_position():
    while True:
        position = input('Position: ').upper()
        if position in POSITIONS:
            return position
        else:
            print('Invalid position. Please try again.')


def get_at_bats():
    while True:
        try:
            at_bats = int(input('At bats: '))
        except ValueError:
            print('Invalid integer. Please try again.')
            continue

        if at_bats < 0 or at_bats > 500:
            print('Invalid entry. Must be between 0 and 500.')
        else:
            return at_bats


def get_hits(at_bats):
    while True:
        try:
            hits = int(input('Hits: '))
        except ValueError:
            print('Invalid integer. Please try again.')
            continue
        if hits < 0 or hits > at_bats:
            print(f"Invalid entry. Must be between 0 and {at_bats}")
        else:
            return hits


def main():
    div_line()
    top_menu()
    div_line()
    players = []
    while True:
        choice = input("Menu option")
        if choice == "1":
            display_lineup(players)
        elif choice == "2":
            add_player()
        elif choice == "3":
            remove_player()
        elif choice == "4":
            move_player()
        elif choice == "5":
            edit_player_pos()
        elif choice == "6":
            edit_player_stat()
        elif choice == "7":
            break
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()
    print("\nBye!")
