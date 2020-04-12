from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.HomeCashierController import HomeCashierController


class HomeCashier_Window(object):

    def __init__(self,username):
        self.username = username
        self.homeCashierController = HomeCashierController(username)
        self.name = self.homeCashierController.checkname()
        self.role = self.homeCashierController.checkrole()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
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
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 370, 101, 21))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 450, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.tabeldata = self.homeCashierController.tabeldata()
        self.allnameitem = self.homeCashierController.getallnameitem()
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 390, 401, 22))
        self.comboBox.setEditable(False)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(510, 390, 111, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(510, 370, 101, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 320, 201, 31))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 781, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(self.tabeldata))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(253)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HomeCashier"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nama:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Role:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"+self.name+"</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"+self.role+"</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Nama Barang</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Jumlah Barang</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Proses Pembelian</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Proses"))
        self.pushButton.clicked.connect(lambda: self.pushProses())
        #tabel
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nama Barang"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Harga ($USD)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Jumlah"))
        for i in range(len(self.tabeldata)):
            count = 0
            for key, value in self.tabeldata[i].items():
                item = QtWidgets.QTableWidgetItem(value)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                if key == "itemname":
                    self.tableWidget.setItem(i, 0, item)
                elif key == "price":
                    self.tableWidget.setItem(i, 1, item)
                elif key == "amountitem":
                    self.tableWidget.setItem(i, 2, item)
                count += 1

        #ComboBox
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Pilih Barang")
        for nameitem in self.allnameitem:
            self.comboBox.addItem(nameitem)

    def pushProses(self):
        itemname = self.comboBox.currentText()
        amoutitem = self.lineEdit.text()
        succses = self.homeCashierController.subAmountitem(itemname,amoutitem)
        if succses:
            self.popupTotalprice(itemname,amoutitem)
            return self.popupSuccess()
        return self.popupFailed()

    def popupTotalprice(self,itemname,amountitem):
        totalprice = self.homeCashierController.gettotalprice(itemname,amountitem)
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Total Harga")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Total Harga = $"+totalprice+"")
        msg.exec_()


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

