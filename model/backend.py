from enum import Enum


@staticmethod
def createVendingProductsByType(product_type):
    assert isinstance(product_type, ProductType)

    vending_products = []
    match product_type:
        case ProductType.coffee:
            vending_products.append(("Coffee", 1.5)),
            vending_products.append(("Hot chocolate", 1)),
            vending_products.append(("Hot water", 0.5)),
        case ProductType.drink:
            vending_products.append(("Coke", 1.2)),
            vending_products.append(("Water", 0.75)),
        case ProductType.snack:
            vending_products.append(("M&Ms", 2.5)),
            vending_products.append(("Chips", 1.9)),
            vending_products.append(("Snickers", 1.3)),
            vending_products.append(("Pantera rosa", 0.7)),
    return vending_products


class VendingProduct:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def price(self):
        return self._price

    def get_name(self):
        return self._name


class Coin:
    def __init__(self, value):
        self._value = value


class ProductType(Enum):
    coffee = 1
    drink = 2
    snack = 3


class ControllerException:
    pass
