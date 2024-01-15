
from dataclasses import dataclass
@dataclass
class product:
    """
    A class to represent a
    """
    name:str
    price:float
    discount:float

    def getDiscountAmount(self):
        """
        Returns the DiscountAmount of the product
        :return:
        """
        return self.price * (self.discount / 100)

    def getDiscountPrice(self):
        """
        Returns the DiscountPrice of the product
        :return:
        """
        return self.price - self.getDiscountAmount()

