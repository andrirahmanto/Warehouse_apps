from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.AddUserController import AddUserController


class AddUser_Window(object):

    def __init__(self,username):
        self.username = username
        self.addUserController = AddUserController(username)
        self.nama = self.addUserController.checkname()
        self.role = self.addUserController.checkrole()
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
        self.label_3.setGeometry(QtCore.QRect(130, 20, 311, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 60, 301, 31))
        self.label_4.setObjectName("label_4")

        self.tabeldata = self.addUserController.tabeldata()
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 781, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(len(self.tabeldata))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(193)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 320, 71, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 340, 121, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 380, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 340, 121, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 320, 71, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(580, 340, 121, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 320, 71, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(430, 400, 121, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 380, 71, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(580, 380, 71, 21))
        self.label_9.setObjectName("label_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 450, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(580, 400, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 490, 141, 51))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "AddUser"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nama:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Role:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"+self.nama+"</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"+self.role+"</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Username</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Username</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Password</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Nama</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Role</span></p></body></html>"))
        # tabel_awal
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nama"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Role"))
        for i in range(len(self.tabeldata)):
            count = 0
            for key, value in self.tabeldata[i].items():
                item = QtWidgets.QTableWidgetItem(value)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                if key == "username":
                    self.tableWidget.setItem(i, 0, item)
                elif key == "password":
                    self.tableWidget.setItem(i, 1, item)
                elif key == "name":
                    self.tableWidget.setItem(i, 2, item)
                elif key == "role":
                    self.tableWidget.setItem(i, 3, item)
                count += 1
        # tabel_akhir
        self.comboBox.setItemText(0, _translate("MainWindow", "Pilih Role"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Admin"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Kasir"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Pengurus Gudang"))
        self.pushButton.setText(_translate("MainWindow", "Hapus Akun"))
        self.pushButton.clicked.connect(lambda: self.pushDeleteAccount())
        self.pushButton_2.setText(_translate("MainWindow", "Buat Akun"))
        self.pushButton_2.clicked.connect(lambda: self.pushAddAccount())
        self.pushButton_3.setText(_translate("MainWindow", "Home"))
        self.pushButton_3.clicked.connect(lambda: self.pushHome())


    def pushHome(self):
        self.MainWindow.close()

    def pushDeleteAccount(self):
        input = self.lineEdit.text()
        succses = self.addUserController.deleteAccount(input)
        if succses:
            return self.popupSuccess()
        return self.popupFailed()

    def pushAddAccount(self):
        username = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        name = self.lineEdit_4.text()
        role = self.comboBox.currentText()
        succses = self.addUserController.addAccount(username,password,name,role)
        if succses:
            return self.popupSuccess()
        return self.popupFailed()

    def popupSuccess(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("WarehouseApp - Success")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Sukses!")
        msg.exec_()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()

    def popupFailed(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("WarehouseApp - Failed")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Input yang ada masukan salah")
        msg.exec_()
