# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urunListesi.ui'
#
# Created: Fri Aug  7 16:21:44 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from PyQt4.QtCore import *
import sys

def main():
    app 	= QApplication(sys.argv)
    return app.exec_()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(472, 448)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(47, 316, 161, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 316, 141, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tableview = QtGui.QTableView(self.centralwidget)
        self.tableview.setGeometry(QtCore.QRect(10, 20, 431, 261))
        self.tableview.setObjectName(_fromUtf8("tableview"))

        db 		= QSqlDatabase.addDatabase("QMYSQL")

        # db connection details
        db.setHostName("127.0.0.1")
        db.setDatabaseName("envanter")
        db.setUserName("root")
        db.setPassword("mek")

        # check fucking connection
        if (db.open()==False):
          QMessageBox.critical(None, "Database Error",
                    db.lastError().text())

        query = QSqlQuery ("SELECT * FROM markalar")

        index=0
        while (query.next()):
            self.tableview.(query.value(1).toString())
            index = index+1

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "UrunListesi", None))
        self.pushButton.setText(_translate("MainWindow", "Guncelle", None))
        self.pushButton_2.setText(_translate("MainWindow", "Sil", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

