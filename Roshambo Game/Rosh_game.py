"""
Rosh game file that will import the rosh classes
to play the game.
"""
from Rosh_classes import Player, Bart, Lisa


def main():
    print("Roshambo Game\n")
    name = input("Enter your name: ")
    print()

    player1 = Player(name)

    opponent = input("Play against Bart or Lisa (b/l): ")
    print()

    if opponent == 'b':
        player2 = Bart()
    elif opponent == 'l':
        player2 = Lisa()
    else:
        print("invalid")

    play_again = 'y'
    while play_again.lower() == "y":
        selection = input("Rock, paper, or scissors (r/p/s): ").lower()
        print()

        if selection == 'r':
            player1.roshambo = "rock"
        elif selection == 'p':
            player1.roshambo = "paper"
        elif selection == 's':
            player1.roshambo = "scissors"
        else:
            print("invalid choice, select again")

        player2.generate_roshambo()

        print(player1)
        print(player2)

        winner = player1.play_roshambo(player2)
        if winner is None:
            print("Draw!")
        else:
            print(f"{winner.name} wins!")
            winner.add_win()
            if winner is player1:
                player2.add_loss()
            else:
                player1.add_loss()

        play_again = input("\nplay again (y/n): ")
        print()

    print(f"{player1.name}: {player1.wins} total win(s), {player1.losses} total loss(es)")
    print(f"{player2.name}: {player2.wins} total win(s), {player2.losses} total loss(es)")


if __name__ == "__main__":
    main()
