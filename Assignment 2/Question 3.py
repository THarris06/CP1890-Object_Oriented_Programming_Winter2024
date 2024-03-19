# Question 3
from dataclasses import dataclass


@dataclass
class Animal:
    name: str
    species: str

    def speak(self):
        print("Sound Here.")


@dataclass
class Dog(Animal):
    breed: str

    def __init__(self, name: str, species: str, breed: str):
        super().__init__(name, species)
        self.breed = breed

    def speak(self):
        print("Woof!")


@dataclass
class Cat(Animal):
    color: str

    def __init__(self, name: str, species: str, color: str):
        super().__init__(name, species)
        self.color = color

    def speak(self):
        print("Meow!")


def main():
    dog = Dog("Max", "Dog", "Golden Retriever")
    cat = Cat("Whiskers", "Cat", "Orange")

    print("Dog:")
    print("Name:", dog.name)
    print("Species:", dog.species)
    print("Breed:", dog.breed)
    print("Sound:", end=" ")
    dog.speak()

    print("\n")

    print("Cat:")
    print("Name:", cat.name)
    print("Species:", cat.species)
    print("Color:", cat.color)
    print("Sound:", end=" ")
    cat.speak()


if __name__ == "__main__":
    main()
