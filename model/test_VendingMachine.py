import unittest
from model.VendingMachine import VendingMachine, _get_coins_value
from model.backend import ProductType


class VendingMachineTestCase(unittest.TestCase):

    def setUp(self):
        self.vm3 = VendingMachine(ProductType.snack)
        self.vm1 = VendingMachine(ProductType.coffee)
        # TODO: Preparar STOCK de monedas y de productos

    def test_get_allowed_coins(self):
        all_coins = self.vm3.get_allowed_coins()
        self.assertEqual(len(all_coins), 4)
        self.assertIn(0.2, all_coins)
        self.assertNotIn(0.2,  self.vm1.get_allowed_coins())

    def test_get_coins_value(self):
        self.assertEqual(_get_coins_value([1, 1, 0.5, 1, 0.2]), 3.7)


if __name__ == '__main__':
    unittest.main()
