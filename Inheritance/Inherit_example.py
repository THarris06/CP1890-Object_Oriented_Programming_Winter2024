
from dataclasses import dataclass


@dataclass
class Product:
    name: str = ''
    price: float = 0.0
    discount_percent: int = 0

    def get_discount_amount(self) -> float:
        return self.price * (self.discount_percent / 100)

    def get_discount_price(self) -> float:
        return self.price - self.get_discount_amount()

    def get_description(self) -> str:
        return self.name


@dataclass
class Book(Product):
    author: str = ""

    def get_description(self) -> str:
        return f"{Product.get_description(self)} by {self.author}"


@dataclass
class Movie(Product):
    year: int = 0

    def get_description(self) -> str:
        return f"{Product.get_description(self)} released in {self.year}"


product1 = Product("Quartet Marker", 2.99, 20)
book1 = Book('The Shining', 12.00, 10, 'Steven King')
movie1 = Movie("Howl's moving castle", 10.99, 10, 2004)


def main(product):
    print("Product Data")
    if isinstance(product, Product):
        print(f"{'Name:':<18}{product.get_description()}")
        if isinstance(product, Book):
            print(f"{'Author:':<18}{product.author}")
        elif isinstance(product, Movie):
            print(f"{'Year:':<18}{product.year}")
        print(f"{'Discount price:':<18}{product.get_discount_price():.2f}")


if __name__ == "__main__":
    main(product1)
    print()
    main(book1)
    print()
    main(movie1)
