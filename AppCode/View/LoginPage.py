# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.LoginPageController import LoginPageController
from View.HomeAdmin import HomeAdmin_Window
from View.HomeCashier import HomeCashier_Window
from View.HomeManagerItem import HomeManagerItem_Window


class LoginPage_Window(object):

    def __init__(self):
        MainWindow = QtWidgets.QMainWindow()
        self.setupUi(MainWindow)
        MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 240, 111, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 240, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 300, 111, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 300, 201, 31))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 70, 241, 61))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 410, 101, 31))
        self.pushButton.setObjectName("pushButton")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "LoginPage"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Username:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Password:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Warehouse App</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton.clicked.connect(lambda: self.pushLogin(MainWindow))

    def pushLogin(self, MainWindow):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        login_controller = LoginPageController(username,password)
        if login_controller.checklogin():
            if login_controller.checkrole() == "Admin":
                self.homeadmin = HomeAdmin_Window(username)
            elif login_controller.checkrole() == "Kasir":
                self.homekasir = HomeCashier_Window(username)
            elif login_controller.checkrole() == "Pengurus Gudang":
                self.homemanageritem = HomeManagerItem_Window(username)
            MainWindow.close()
        else:
            self.popupWrongLogin()

    def popupWrongLogin(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Peringatan!!")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Username atau password salah!")
        msg.exec_()

