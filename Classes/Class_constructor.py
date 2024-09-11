class product:

    def __init__(self, name = "", price = 0.0, discount = 0):
        self.name = name
        self.price = price
        self.discount = discount

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

