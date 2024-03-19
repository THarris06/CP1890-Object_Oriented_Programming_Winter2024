from dataclasses import dataclass
from random import randint


@dataclass
class RandomIntList(list):
    """
    Class to represent a list of random integers.
    get_count() - returns the length of the list.
    get_total() - returns the total sum of the numbers in the list.
    get_avg() - returns the average of the numbers in the list.
    """
    num: int

    def __post_init__(self):
        for num in range(self.num):
            self.append(randint(0, 100))

    def __str__(self):
        return ', '.join(map(str, self))

    def get_count(self):
        return len(self)

    def get_total(self):
        return sum(self)

    def get_avg(self):
        return sum(self) / len(self)


def main():
    print("Random Integer List")

    loop = 'y'
    num = int(input("\nHow many random integers should the list contain?: "))

    while loop.lower() == 'y':
        int_list = RandomIntList(num)
        print("\nRandom Integers")
        print("===============")
        print(f"{'Integers:':<11} {int_list}")
        print(f"{'Count':<11} {int_list.get_count()}")
        print(f"{'Total':<11} {int_list.get_total()}")
        print(f"{'Average':<11} {int_list.get_avg():.3f}")

        loop = input("\nContinue (y/n): ").lower()


if __name__ == '__main__':

    main()
    print("\nBye!")
