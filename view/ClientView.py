from PyQt5 import QtWidgets, QtCore
from model.backend import ProductType


class ClientView(QtWidgets.QWidget):

    insert_coin_signal = QtCore.pyqtSignal(float)
    retrieve_money_signal = QtCore.pyqtSignal(float)
    credit_changed_signal = QtCore.pyqtSignal(float)
    buy_product_signal = QtCore.pyqtSignal(str, float)

    def __init__(self, products, coins):
        super().__init__()
        self.products = products    # list of pairs (name-prize)
        self.coins = coins          # list of floats
        self.client_credit = 0.0    # float
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Vending Machine')
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.set_insert_coin_layout()
        self.set_buy_product_layout()
        # self.insert_coin_signal.connect(lambda coin: self.credit_widget.display(str(coin)))

    def set_insert_coin_layout(self):
        # coins_label = QtWidgets.QLabel("Insert Coin")
        self.gb = QtWidgets.QGroupBox("Insert Coin", self)
        gr_lo = QtWidgets.QVBoxLayout()
        self.credit_widget = QtWidgets.QLCDNumber()
        self.credit_changed_signal.connect(self.credit_widget.display)
        self.credit_widget.display(str(self.client_credit))
        coin_layout = QtWidgets.QHBoxLayout()
        for coin in self.coins:
            btn = QtWidgets.QPushButton(str(coin))
            btn.clicked.connect(self._emit_insert_coin_signal(coin))
            coin_layout.addWidget(btn)
        gr_lo.addLayout(coin_layout)
        credit_layout = QtWidgets.QHBoxLayout()
        credit_label = QtWidgets.QLabel("Credit:")
        credit_layout.addWidget(credit_label)
        credit_layout.addWidget(self.credit_widget)
        self.retrieve_btn = QtWidgets.QPushButton("Retrieve money")
        self.retrieve_btn.clicked.connect(lambda: self.retrieve_money_signal.emit(self.client_credit))
        credit_layout.addWidget(self.retrieve_btn)
        gr_lo.addLayout(credit_layout)
        # gr_lo.addWidget(self.credit_widget)
        self.gb.setLayout(gr_lo)
        self.main_layout.addWidget(self.gb)

    def _emit_insert_coin_signal(self, coin):
        return lambda: self.insert_coin_signal.emit(coin)

    def _emit_buy_product_signal(self, name, prize):
        return lambda: self.buy_product_signal.emit(name, prize)

    def _connect_check_button_availability(self, btn, price):
        assert isinstance(btn, QtWidgets.QPushButton)
        return lambda: self._check_button_availability(btn, price)

    def _check_button_availability(self, btn, price):
        x = True if self.client_credit < price else False
        btn.setDisabled(x)

    def set_buy_product_layout(self):
        # products_label = QtWidgets.QLabel("Buy Product")
        products_layout = QtWidgets.QHBoxLayout()
        for name, prize in self.products:
            lbl = QtWidgets.QLabel("prize: %.2f €" % prize)
            btn = QtWidgets.QPushButton(name)
            self.credit_changed_signal.connect(self._connect_check_button_availability(btn, prize))
            btn.clicked.connect(self._emit_buy_product_signal(name, prize))
            btn.setDisabled(True)
            vboxlayout = QtWidgets.QVBoxLayout()
            vboxlayout.addWidget(btn)
            vboxlayout.addWidget(lbl)
            products_layout.addLayout(vboxlayout)
        self.gb = QtWidgets.QGroupBox("Buy Product", self)
        gr_lo = QtWidgets.QVBoxLayout()
        gr_lo.addLayout(products_layout)
        self.gb.setLayout(gr_lo)
        self.main_layout.addWidget(self.gb)
