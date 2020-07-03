from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import res, json
from PyQt5 import QtCore

class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi("login.ui", self)

class MenuBar(QWidget):
    def __init__(self):
        super(MenuBar, self).__init__()
        uic.loadUi("menubar.ui", self)

class Item(QWidget):
    procStart = QtCore.pyqtSignal(dict)
    def __init__(self):
        super(Item, self).__init__()
        uic.loadUi("product.ui", self)
    #     self.data = Dashboard()

    # @QtCore.pyqtSlot()
    # def on_button_clicked(self, data):
    #     self.procStart.emit(self.data.getdata())


class Cart(QWidget):
    def __init__(self):
        super(Cart, self).__init__()
        uic.loadUi("cart.ui", self)
        # label = self.findChild(QLabel, "label_3")
        # label.setText("wahyu")
    #     self.dataProd = []

    # @QtCore.pyqtSlot(dict)
    # def on_item_procstart(self, data):
    #     self.dataProd.append(data)


class Dashboard(QMainWindow):
    def __init__(self):
        super(Dashboard, self).__init__()
        self.menu = MenuBar()
        self.cart = Cart()
        self.dataProduk = self.fetch()
        self.mainUi()
        self.setCentralWidget(self.vWidget)

    def fetch(self):
        with open('product.json', 'r') as product:
            data = json.load(product)
        return data


    def mainUi(self):
        cover = ["download.jpg", "teahot.jpg", "alpukatjus.jpg", "mangga.jpg"]
        # allBtn = self.menu.findChild(QPushButton, "btnAll")
        # tehBtn = self.menu.findChild(QPushButton, "btnTeh")
        # dataProd = list(filter(lambda a: a['category'] == 'teh', self.dataProduk))
        dataProd = self.dataProduk
        self.hLayout = QHBoxLayout()
        for x in range(len(dataProd)):
            self.item = Item()
            self.hLayout.addWidget(self.item)
            pixmap = QPixmap("./Img/{}".format(cover[x]))
            labelImg = self.item.findChild(QLabel, "labelImage")
            labelImg.setPixmap(pixmap)
            nama = self.item.findChild(QLabel, "namaProd")
            nama.setText(dataProd[x]["nama"])
            harga = self.item.findChild(QLabel, "priceIceTea")
            harga.setText(dataProd[x]["harga"])
            desk = self.item.findChild(QLabel, "deskLabel")
            desk.setText(dataProd[x]["deskripsi"])
            self.addToCart = {"nama": dataProd[x], "harga": dataProd[x]["harga"]}
            self.item.btnAdd.clicked.connect(self.getdata)

        self.hLayout.addWidget(self.cart)
        self.hWidget = QWidget()
        self.hWidget.setLayout(self.hLayout)

        self.vLayout = QVBoxLayout()
        self.vLayout.addWidget(self.menu)
        self.vLayout.addWidget(self.hWidget)
        self.vLayout.setStretch(0, 90)
        self.vLayout.setStretch(1, 1000)

        self.vWidget = QWidget()
        self.vWidget.setLayout(self.vLayout)

    def getdata(self):
        return self.addToCart


    # def ok(self):
    #     print("Ok")


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.mainUi()
        self.mainLayout()

        # self.product = Item()
        # self.cart = Cart()

        # self.product.procStart(self.cart.on_item_procstart)


    def mainUi(self):
        self.login = Login()
        self.dashboard= Dashboard()
        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(self.login)
        self.stackedLayout.addWidget(self.dashboard)
        self.login.btnLogin.clicked.connect(self.act_login)
        logout = self.dashboard.findChild(QPushButton, "btnLogout")
        logout.clicked.connect(self.act_logout)

    def mainLayout(self):
        self.widget = QWidget()
        # self.widget.setStyleSheet("background-color: rgb(46, 109, 255)")
        self.widget.setLayout(self.stackedLayout)
        self.setCentralWidget(self.widget)

    def act_login(self):
        self.stackedLayout.setCurrentIndex(1)

    def act_logout(self):
        self.stackedLayout.setCurrentIndex(0)




if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec_()