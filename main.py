if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets
    from view.InitialView import InitialView
    from controller.VendingController import VendingController

    app = QtWidgets.QApplication(sys.argv)
    main = VendingController()
    sys.exit(app.exec_())

    # v = VendingMachine("asfd")
    # d = {0.1: 3}
    # v.add_coins(d)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
