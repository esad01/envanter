# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PROJE.ui'
#
# Created: Thu Aug  6 15:36:14 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtSql import *
from PyQt4.QtGui import *

db = QSqlDatabase.addDatabase("QMYSQL")
db.setHostName("127.0.0.1")
db.setDatabaseName("envanter")
db.setUserName("root")
db.setPassword("mek")

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
        MainWindow.resize(582, 384)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 50, 481, 281))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(340, 30, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(180, 170, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(10, 70, 91, 27))

        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox_2 = QtGui.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 70, 101, 27))

        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))

        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.comboBox_3 = QtGui.QComboBox(self.tab_2)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 70, 101, 27))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))

        self.comboBox_4 = QtGui.QComboBox(self.tab_2)
        self.comboBox_4.setGeometry(QtCore.QRect(310, 70, 111, 31))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))

        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 176, 131, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(330, 30, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_5 = QtGui.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 66, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(320, 30, 66, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.comboBox_5 = QtGui.QComboBox(self.tab_3)
        self.comboBox_5.setGeometry(QtCore.QRect(10, 70, 91, 27))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))

        self.comboBox_6 = QtGui.QComboBox(self.tab_3)
        self.comboBox_6.setGeometry(QtCore.QRect(310, 70, 101, 27))
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))

        self.pushButton_7 = QtGui.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(160, 170, 98, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.label_7 = QtGui.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(20, 40, 91, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit = QtGui.QLineEdit(self.tab_4)
        self.lineEdit.setGeometry(QtCore.QRect(110, 40, 291, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_10 = QtGui.QPushButton(self.tab_4)
        self.pushButton_10.setGeometry(QtCore.QRect(167, 110, 131, 31))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.pushButton_11 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(340, 10, 98, 27))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_12 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(450, 10, 98, 27))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Urun Verileri", None))
        self.label.setText(_translate("MainWindow", "Marka", None))
        self.label_2.setText(_translate("MainWindow", "CihazTipi", None))
        self.pushButton.setText(_translate("MainWindow", "Add", None))

       #COMBO1
        table 	= QTableWidget()
        db 		= QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName("127.0.0.1")
        db.setDatabaseName("envanter")
        db.setUserName("root")
        db.setPassword("mek")

        if (db.open()==False):
          QMessageBox.critical(None, "Database Error",
                    db.lastError().text())

        query = QSqlQuery ("SELECT * FROM markalar")

        table.setColumnCount(query.record().count())
        table.setRowCount(query.size())

        index=0
        while (query.next()):
            table.setItem(index,1,self.comboBox.addItem(query.value(1).toString()))

        index = index+1

        self.comboBox.show()

        #COMBO2

        table 	= QTableWidget()
        db 		= QSqlDatabase.addDatabase("QMYSQL")

        db.setHostName("127.0.0.1")
        db.setDatabaseName("envanter")
        db.setUserName("root")
        db.setPassword("mek")

        if (db.open()==False):
          QMessageBox.critical(None, "Database Error",
                    db.lastError().text())

        query = QSqlQuery ("SELECT * FROM cihazTipleri")

        table.setColumnCount(query.record().count())
        table.setRowCount(query.size())

        index=0
        while (query.next()):
            table.setItem(index,1,self.comboBox_2.addItem(query.value(1).toString()))

        index = index+1

        self.comboBox_2.show()



        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Depo", None))

        #COMBO3
        table 	= QTableWidget()
        db 		= QSqlDatabase.addDatabase("QMYSQL")

        db.setHostName("127.0.0.1")
        db.setDatabaseName("envanter")
        db.setUserName("root")
        db.setPassword("mek")

        if (db.open()==False):
          QMessageBox.critical(None, "Database Error",
                    db.lastError().text())

        query = QSqlQuery ("SELECT * FROM markalar")

        table.setColumnCount(query.record().count())
        table.setRowCount(query.size())

        index=0
        while (query.next()):
            table.setItem(index,1,self.comboBox_3.addItem(query.value(1).toString()))

        index = index+1

        self.comboBox_3.show()

        #COMBO4

        table 	= QTableWidget()
        db 		= QSqlDatabase.addDatabase("QMYSQL")

        db.setHostName("127.0.0.1")
        db.setDatabaseName("envanter")
        db.setUserName("root")
        db.setPassword("mek")

        if (db.open()==False):
          QMessageBox.critical(None, "Database Error",
                    db.lastError().text())

        query = QSqlQuery ("SELECT * FROM cihazTipleri")

        table.setColumnCount(query.record().count())
        table.setRowCount(query.size())

        index=0
        while (query.next()):
            table.setItem(index,1,self.comboBox_4.addItem(query.value(1).toString()))

        index = index+1

        self.comboBox_4.show()



        self.pushButton_4.setText(_translate("MainWindow", "Add", None))
        self.label_3.setText(_translate("MainWindow", "Marka", None))
        self.label_4.setText(_translate("MainWindow", "CihazTipi", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Sistem", None))
        self.label_5.setText(_translate("MainWindow", "Marka", None))
        self.label_6.setText(_translate("MainWindow", "CihazTipi", None))

      #COMBO5

        table 	= QTableWidget()
        db 		= QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName("127.0.0.1")
        db.setDatabaseName("envanter")
        db.setUserName("root")
        db.setPassword("mek")

        if (db.open()==False):
          QMessageBox.critical(None, "Database Error",
                    db.lastError().text())

        query = QSqlQuery ("SELECT * FROM markalar")

        table.setColumnCount(query.record().count())
        table.setRowCount(query.size())

        index=0
        while (query.next()):
            table.setItem(index,1,self.comboBox_5.addItem(query.value(1).toString()))

        index = index+1

        self.comboBox_5.show()

        #COMBO6

        table 	= QTableWidget()
        db 		= QSqlDatabase.addDatabase("QMYSQL")

        db.setHostName("127.0.0.1")
        db.setDatabaseName("envanter")
        db.setUserName("root")
        db.setPassword("mek")

        if (db.open()==False):
          QMessageBox.critical(None, "Database Error",
                    db.lastError().text())

        query = QSqlQuery ("SELECT * FROM cihazTipleri")

        table.setColumnCount(query.record().count())
        table.setRowCount(query.size())

        index=0
        while (query.next()):
            table.setItem(index,1,self.comboBox_6.addItem(query.value(1).toString()))

        index = index+1

        self.comboBox_6.show()




        self.pushButton_7.setText(_translate("MainWindow", "Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "FKM", None))
        self.label_7.setText(_translate("MainWindow", "SeriNo", None))
        self.pushButton_10.setText(_translate("MainWindow", "Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Search", None))
        self.pushButton_11.setText(_translate("MainWindow", "Marka Ekle", None))
        self.pushButton_12.setText(_translate("MainWindow", "CihazTipi Ekle", None))

   

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

