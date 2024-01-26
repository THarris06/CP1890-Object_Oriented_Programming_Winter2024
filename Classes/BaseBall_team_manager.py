from datetime import datetime


def div_line():
    print("="*50)


def top_menu():
    print(f"{'BaseBall Team Manager':>50}")

    cur_date = datetime.now().date()
    print("CURRENT DATE:")

    print("DAYS UNTIL GAME: 2")
    print()
    print("1. - Display lineup")
    print("2. - Add player")
    print("3. - Remove player")
    print("4. - Move player")
    print("5. - Edit player position")
    print("6. - Edit player stats")
    print("7. - Exit program\n")
    print("Positions")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")


