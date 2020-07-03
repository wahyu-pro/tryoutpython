from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
from PyQt5 import uic
import res

class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi("login.ui", self)

class MenuBar(QWidget):
    def __init__(self):
        super(MenuBar, self).__init__()
        uic.loadUi("menubar.ui", self)

class Item(QWidget):
    def __init__(self):
        super(Item, self).__init__()
        uic.loadUi("item.ui", self)

class Cart(QWidget):
    def __init__(self):
        super(Cart, self).__init__()
        uic.loadUi("cart.ui", self)


class Dashboard(QMainWindow):
    def __init__(self):
        super(Dashboard, self).__init__()
        self.menu = MenuBar()
        self.item = Item()
        self.cart = Cart()
        self.mainUi()
        self.setCentralWidget(self.vWidget)

    def mainUi(self):
        self.hLayout = QHBoxLayout()
        self.hLayout.addWidget(self.item)
        self.hLayout.addWidget(self.cart)
        for x in range(3):
            self.hLayout.addWidget(Item())
            # for a in range(3):
                # self. v_product = QVBoxLayout()
                # self.v_product.addWidget(self.item)
        # self.hLayout.setStretch(0, 1500)
        # self.hLayout.setStretch(1, 300)
        self.hWidget = QWidget()
        self.hWidget.setLayout(self.hLayout)

        self.vLayout = QVBoxLayout()
        self.vLayout.addWidget(self.menu)
        self.vLayout.addWidget(self.hWidget)
        self.vLayout.setStretch(0, 90)
        self.vLayout.setStretch(1, 1000)

        self.vWidget = QWidget()
        self.vWidget.setLayout(self.vLayout)

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.mainUi()
        self.mainLayout()


    def mainUi(self):
        self.login = Login()
        self.dashboard= Dashboard()
        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(self.login)
        self.stackedLayout.addWidget(self.dashboard)
        self.login.btnLogin.clicked.connect(self.act_login)

    def mainLayout(self):
        self.widget = QWidget()
        # self.widget.setStyleSheet("background-color: rgb(46, 109, 255)")
        self.widget.setLayout(self.stackedLayout)
        self.setCentralWidget(self.widget)

    def act_login(self):
        self.stackedLayout.setCurrentIndex(1)




if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()