from model.backend import *


def _get_coins_value(coins):
    suma = 0
    for coin in coins:
        suma += coin
    return suma


class VendingMachine:

    def __init__(self, product_type):
        assert isinstance(product_type, ProductType), "The initial parameter must be a ProductType class"

        self._productType = product_type
        self._typeProducts = []     # list of VendingProducts
        self._vendingStock = {}     # dict (VendingProducts.get_name()->items)
        self._coins = {}            # dict (coin->items)
        self._init_vending_products()
        self._init_machine_coins()
        self._init_vending_stock()

    def _init_vending_products(self):
        for name, price in createVendingProductsByType(self._productType):
            self._typeProducts.append(VendingProduct(name, price))

    def _init_vending_stock(self):
        for product in self._typeProducts:
            if isinstance(product, VendingProduct):
                self._vendingStock[product.get_name()] = 0

    def _init_machine_coins(self):
        match self._productType:
            case ProductType.coffee:
                self._coins = dict([
                    (0.5, 0),
                    (1, 0),
                ])
            case ProductType.drink:
                self._coins = dict([
                    (0.05, 0),
                    (0.1, 0),
                    (0.2, 0),
                    (0.5, 0),
                    (1, 0),
                ])
            case ProductType.snack:
                self._coins = dict([
                    (0.1, 0),
                    (0.2, 0),
                    (0.5, 0),
                    (1, 0),
                ])

    def set_coins(self, coins):
        # Fill the machine for Exchange
        if isinstance(coins, dict):
            self._coins.update(coins)

    def add_coins(self, coins):
        # Fill the machine for Exchange
        if isinstance(coins, dict):
            for value, num in coins.items():
                self._coins[value] += num

    def add_coin(self, coin):
        # Insert Coin feature
        assert isinstance(coin, float)
        self._coins[coin] += 1

    def _remove_coin(self, coin):
        # For exchange
        if isinstance(coin, float):
            raise (TypeError, "coin must be a float")
        self._coins[coin] -= 1
        if self._coins[coin] < 0:
            raise ControllerException

    def get_coins(self, coin):
        # give the number of coins the machine has with 'coin' value.
        if isinstance(coin, float):
            raise (TypeError, "coin must be a float")
        return self._coins[coin]

    def set_vending_stock(self, stock):
        # Fill the machine with products
        if isinstance(stock, dict):
            self._vendingStock.update(stock)

    def get_stock(self):
        # return the pairs (name-units) for every product
        return self._vendingStock

    def add_products(self, products):
        # Fill the machine with products
        if isinstance(products, dict):
            for name, num in products.items():
                self._vendingStock[name] += num

    # TODO
    def sell_product(self, product, coins):
        # @coins = list of floats
        # Updates the stock without one item of 'product' and the coins for the price
        # Return the coins back for the exchange if needed
        assert isinstance(product, VendingProduct)
        assert self._vendingStock[product.get_name()] > 0
        assert _get_coins_value(coins) >= product.price
        self._vendingStock[product.get_name()] -= 1
        # falta deixar monedes i treure canvi
        exchange = 0
        return exchange

    def get_products(self):
        # return VendingProduct list
        return self._typeProducts

    def get_allowed_coins(self):
        # return a list of floats
        return list(self._coins.keys())
