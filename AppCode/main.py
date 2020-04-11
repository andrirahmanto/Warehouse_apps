from View.LoginPage import LoginPage_Window
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Main:

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        login = LoginPage_Window()
        sys.exit(app.exec_())

if __name__ == "__main__":
    m = Main()
    m.run()