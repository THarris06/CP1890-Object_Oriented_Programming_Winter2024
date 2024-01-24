
class product:

    def __init__(self, p_name, p_price, p_discount_percent):
        self.name: str = p_name
        self.__price: float = p_price
        self.discount_percent: float = p_discount_percent

    def __post_init__(self):
        self.p_price = self.__price

    @property
    def price(self) -> float:
        return float(self.__price)

    @price.setter
    def price(self, p_price: float):
        if p_price < 0:
            raise ValueError("Price cannot be less than 0)")
        else:
            self.__price = p_price

    def get_discount_amount(self):
        return self.__price * (self.discount_percent / 100)

    def get_discount_price(self):
        return self.__price - self.get_discount_amount()
