from pig_dice_roll_classes import Game


def title():
    print("Lets play Pig!\n")
    print("* See how many turns it takes you to get to 20.\n")
    print("* Turn ends when you hold or roll a 1.\n")
    print("* If you roll a 1, you lose all points for the turn.\n")
    print("* If you hold, you save all points for the turn.\n")


def main():
    title()
    choice = "y"
    while choice.lower() == "y":
        game = Game()
        game.play()

        choice = input("Play again (y/n):")
        print()

    print("Thank you for playing!")


if __name__ == "__main__":
    main()
