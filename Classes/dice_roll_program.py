
from encapsulation_die_class_object import Die, Dice


def title():
    print("The Dice Roll Program\n")


def get_die_amount():
    num_dice = int(input("Enter the number of dice to roll: "))
    return num_dice


def main():
    title()
    loop = 'y'

    dice_num = get_die_amount()
    dice = Dice()
    for i in range(dice_num):
        die = Die()
        dice.add_die(die)

    while loop.lower() == 'y':
        dice.roll_all()

        print("YOUR ROLL: ", end="")
        for die in dice.list_dice:
            print(die.getvalue(), end=" ")
        print()

        loop = input("Roll again? (y/n): ").lower()

    print("Bye!")


if __name__ == "__main__":
    main()
