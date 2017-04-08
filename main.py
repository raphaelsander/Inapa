import sys
from PyQt4 import QtGui
from PyQt4.uic import loadUiType
from get import *

Ui_MainWindow, QMainWindow = loadUiType('ui/main.ui')
Ui_LoginWindow, QLoginWindow = loadUiType('ui/login.ui')

class Login(QLoginWindow, Ui_LoginWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)

    def on_lineEdit_textEdited(self, text):
        self.matr = text

    def on_lineEdit_2_textEdited(self, text):
        self.senha = text

    def on_comboBox_activated(self, QString):
        self.curso = QString

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

    def provas(self):

        lista_provas = get_provas("000", "000000", "21")

        num_itens = len(lista_provas)/7
        self.tableWidget.setRowCount(num_itens)

        cont = cont2 = 0

        for iten in lista_provas:
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(cont2, cont, item)
            item.setText("%s" % iten)

            cont = cont + 1

            if cont == 7:
                cont2 = cont2 + 1
                cont = 0

if __name__ == '__main__' :
	app = QtGui.QApplication(sys.argv)
	main = Main()
	main.show()
	sys.exit(app.exec_())