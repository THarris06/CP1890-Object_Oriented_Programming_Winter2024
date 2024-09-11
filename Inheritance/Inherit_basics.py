from dataclasses import dataclass


@dataclass
class Product:
    name: str = ""
    price: float = 0.0
    discount_percent: int = 0

    def get_discount_amount(self) -> float:
        return self.price * (self.discount_percent/100)

    def get_discount_price(self) -> float:
        return self.price - self.get_discount_amount()

    def get_description(self) -> str:
        return self.name
 
    def __str__(self):
        return self.name + "is actually Thor's Hammer."

    def __eq__(self, other):
        return self.name == other.name


@dataclass
class Book(Product):
    author: str = ""

    def get_description(self) -> str:
        return f"{Product.get_description(self)} by {self.author}"

# class Book(Product):
#     def __init__(self, name: str = '', price: float = 0.0, discount_percent: int = 0, author=""):
#         Product.__init__(self, name, price, discount_percent)
#
#         self.author = author
#
#     def get_description(self) -> str:
#         return f"{Product.get_description(self)} by {self.author}"


@dataclass
class Movie(Product):
    year: int = 0

    def get_description(self) -> str:
        return f"{Product.get_description(self)} released in {self.year}"


if __name__ == "__main__":

    product1 = Product("Quartet Marker", 2.99, 20)
    book1 = Book('The Shining', 12.00, 10, 'Steven King')
    movie1 = Movie("Howl's moving castle", 10.99, 10, 2004)

    print(product1.get_description())
    print(book1.get_description())
    print(movie1.get_description())

    print(isinstance(movie1, Movie))
    print(isinstance(movie1, Product))
    print(isinstance(movie1, Book))
