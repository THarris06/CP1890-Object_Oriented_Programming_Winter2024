from dataclasses import dataclass


@dataclass
class Animal:
    """
    Animal is a class that represents a generic animal
    with a name and species
    speak() - will return No sound until overwritten in subclass.
    """
    def __init__(self, name="", species=""):
        self.name: str = name
        self.species: str = species

    def speak(self):
        return None


class Dog(Animal):
    """
    Subclass of Animal this class represents a dog
    and breed is add as an attribute
    Speak() - is override in subclass to return a sound.
    """
    def __init__(self, name="", species="", breed=""):
        super(Dog, self).__init__(name, species)
        self.breed: str = breed

    def speak(self):
        print("Woof!")


@dataclass
class Cat(Animal):
    """
    Subclass of Animal this class represents a cat
    and colour is add as an attribute
    Speak() - is override in subclass to return a sound.
    """
    def __init__(self, name="", species="", colour=""):
        super(Cat, self).__init__(name, species)
        self.colour: str = colour

    def speak(self):
        print("Meow!")


def main():
    dog = Dog("max", "dog", "Golden Retriever")
    cat = Cat("Whiskers", "Cat", "Orange")

    print("Dog:")
    print("Name:", dog.name)
    print("Species:", dog.species)
    print("Breed:", dog.breed)
    print("Sound:", end=" ")
    dog.speak()
    print()
    print("Cat:")
    print("Name:", cat.name)
    print("Species:", cat.species)
    print("Color:", cat.colour)
    print("Sound:", end=" ")
    cat.speak()


if __name__ == "__main__":
    main()
    print("\nBye!")
