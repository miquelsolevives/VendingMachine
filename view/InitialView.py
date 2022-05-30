from PyQt5 import QtWidgets, QtCore
# from controller.VendingController import VendingController
# from model.VendingMachine import VendingMachine
from model.backend import ProductType


class InitialView(QtWidgets.QWidget):

    machine_type_signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_view()

    def init_view(self):
        self.setWindowTitle('Vending Machine')
        self.label = QtWidgets.QLabel("Which kind of vending machine am I?", self)
        self.combo = QtWidgets.QComboBox(self)
        self.combo.addItems([name for name, member in ProductType.__members__.items()])
        self.ok_button = QtWidgets.QPushButton("OK", self)
        # self.ok_button.clicked.connect(lambda: self.startMachine(self.combo))
        self.ok_button.clicked.connect(lambda: self.machine_type_signal.emit(self.combo.currentText()))
        self.layout = QtWidgets.QFormLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.combo)
        self.layout.addWidget(self.ok_button)

    # def startMachine(self, product_type_combo):
    #     product_type = ProductType[product_type_combo.currentText()]
    #     self.v_machine = VendingMachine(product_type)
    #     self.controller = VendingController(product_type)

    # def emit_machine_type_signal(self):
    #     self.machine_type_signal.emit(self.combo.currentText())