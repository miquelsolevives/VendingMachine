from PyQt5 import QtWidgets, QtGui

import main
from view.ClientView import ClientView
from model.VendingMachine import VendingMachine
from model.backend import ProductType, VendingProduct
from view.InitialView import InitialView


class VendingController(object):
    admin = False  # TO DO

    def __init__(self):
        self.initial_view = InitialView()
        self.initial_view.machine_type_signal.connect(self.init_vending_machine)
        self.initial_view.show()

    def init_vending_machine(self, product_type_str):
        # [assert isinstance(product_type, ProductType)]
        self.v_machine = VendingMachine(ProductType[product_type_str])

        if VendingController.admin:
            self.init_admin_view()
        else:
            self.init_client_view()
            self._credit_coins = []

        self.initial_view.close()

    def init_client_view(self):
        product_list = self.v_machine.get_products()
        product_list_info = []
        for prod in product_list:
            if isinstance(prod, VendingProduct):
                product_list_info.append([prod.get_name(), prod.price])
        coins_list = self.v_machine.get_allowed_coins()
        # print(product_list_info)
        # print(coins_list)
        self.client_view = ClientView(product_list_info, coins_list)
        self.client_view.insert_coin_signal.connect(self.update_credit)
        self.client_view.buy_product_signal.connect(self.buy_product)
        self.client_view.retrieve_money_signal.connect(self.retrieve_money)
        self.client_view.show()

    def update_credit(self, coin):
        assert isinstance(coin, float)
        self.client_view.client_credit += coin
        self._credit_coins.append(coin)
        # self.client_view.credit_widget.display(str(self.client_view.client_credit))
        self.client_view.credit_changed_signal.emit(self.client_view.client_credit)
        #QtWidgets.QMessageBox.information(self.client_view, 'Success', str(self.client_view.client_credit), QtWidgets.QMessageBox.Ok)
        # self.v_machine.add_coin(coin)   # Update the model
        self._check_available_products()

    def buy_product(self, name, prize):

        print(name)
        print(prize)

    # TO DO
    def _check_available_products(self):
        pass

    def retrieve_money(self, amount):
        self.client_view.client_credit = 0
        self.client_view.credit_changed_signal.emit(0)
        self._credit_coins.clear()
        # self.client_view.credit_widget.display(str(self.client_view.client_credit))
        print(amount)
