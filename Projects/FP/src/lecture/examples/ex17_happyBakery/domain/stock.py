class Stock:
    """
    Represents a unit of bakery stock
    """

    def __init__(self, stock_item, quantity):
        self._stockItem = stock_item
        self.quantity = quantity

    @property
    def item(self):
        """
        Ingredient or Product
        """
        return self._stockItem

    @property
    def quantity(self):
        """
        Available quantity
        """
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Stock cannot fall below 0!")
        self._quantity = value


class StockValidator:
    @staticmethod
    def validate(stock):
        # TODO Implement
        pass
