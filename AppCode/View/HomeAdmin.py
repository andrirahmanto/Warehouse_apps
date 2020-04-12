from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.HomeController import HomeController
from View.ShowAllItem import ShowAllItem_Window
from View.ShowTransacrion import ShowTransaction_Window
from View.AddUser import AddUser_Window


class HomeAdmin_Window(object):

    def __init__(self, username):
        self.username = username
        self.homecontroller = HomeController(username)
        self.name = self.homecontroller.checkname()
        self.role = self.homecontroller.checkrole()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 111, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 20, 300, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 60, 300, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 200, 181, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 270, 181, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 340, 181, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HomeAdmin"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nama:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Role:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"+self.name+"</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"+self.role+"</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Lihat Semua Barang"))
        self.pushButton.clicked.connect(lambda: self.pushShowAllItem())
        self.pushButton_2.setText(_translate("MainWindow", "Lihat Transaksi"))
        self.pushButton_2.clicked.connect(lambda: self.pushShowTransaction())
        self.pushButton_3.setText(_translate("MainWindow", "Tambah / Hapus Akun"))
        self.pushButton_3.clicked.connect(lambda: self.pushAddUser())


    def pushShowAllItem(self):
        self.ShowAllItem = ShowAllItem_Window(self.username)

    def pushShowTransaction(self):
        self.ShowTransaction = ShowTransaction_Window(self.username)

    def pushAddUser(self):
        self.AddUser = AddUser_Window(self.username)





