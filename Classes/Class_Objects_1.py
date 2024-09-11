
from dataclasses import dataclass


@dataclass
class product:
    """
    A class to represent a
    """
    name: str = ''
    price: float = 0.0
    discount: float = 0.0

    def get_discount_amount(self):
        """
        Returns the DiscountAmount of the product
        :return:
        """
        return self.price * (self.discount / 100)

    def get_discount_price(self):
        """
        Returns the DiscountPrice of the product
        :return:
        """
        return self.price - self.get_discount_amount()
