__author__ = 'mek'

from PyQt4.QtGui import *
from PyQt4.QtSql import *
from PyQt4.QtCore import *
import sys

def main():
    app 	= QApplication(sys.argv)
    table 	= QTableWidget()
    db 		= QSqlDatabase.addDatabase("QMYSQL")

    db.setHostName("127.0.0.1")
    db.setDatabaseName("envanter")
    db.setUserName("root")
    db.setPassword("mek")

    combo = QComboBox()

    if (db.open()==False):
      QMessageBox.critical(None, "Database Error",
			    db.lastError().text())

    query = QSqlQuery ("SELECT * FROM markalar")

    table.setColumnCount(query.record().count())
    table.setRowCount(query.size())

    index=0
    while (query.next()):
	table.setItem(index,1,combo.addItem(query.value(1).toString()))

	index = index+1

    combo.show()

    return app.exec_()
if __name__ == '__main__':
  main()