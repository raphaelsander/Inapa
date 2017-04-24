#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4.uic import loadUiType
from get import *

Ui_MainWindow, QMainWindow = loadUiType('ui/main.ui')
Ui_LoginWindow, QLoginWindow = loadUiType('ui/login.ui')

class Login(QLoginWindow, Ui_LoginWindow):
    def __init__(self):
        QLoginWindow.__init__(self)
        self.setupUi(self)

        self.label_4.hide()
        self.gif_loading = QtGui.QMovie("ui/loading.gif")
        self.label_4.setMovie(self.gif_loading)
        self.gif_loading.start()

    def on_lineEdit_textEdited(self, text):
        self.matr = text

    def on_lineEdit_2_textEdited(self, text):
        self.senha = text

    def on_comboBox_currentIndexChanged(self, int):
        if int == 0:
            self.curso = "1"
        if int == 1:
            self.curso = "2"
        if int == 2:
            self.curso = "12"
        if int == 3:
            self.curso = "6"
        if int == 4:
            self.curso = "24"
        if int == 5:
            self.curso = "5"
        if int == 6:
            self.curso = "7"
        if int == 7:
            self.curso = "21"
        if int == 8:
            self.curso = "31"

    def on_pushButton_pressed(self):
        self.label_4.show()
        hey = Main(self.matr, self.senha, self.curso)
        hey.provas()
        hey.horario()
        hey.show()
        login.hide()
        hey.exec_()

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, matr, senha, curso):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.matr = matr
        self.senha = senha
        self.curso = curso

    def provas(self):

        lista_provas = get_provas(self.matr, self.senha, self.curso)

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

    def horario(self):

        lista_horario = get_horario(self.matr, self.senha, self.curso)

        cont = cont2 = 0

        for iten in lista_horario:
            item = QtGui.QTableWidgetItem()
            self.tableWidget_2.setItem(cont2, cont, item)
            item.setText("%s" % iten)

            cont = cont + 1

            if cont == 6:
                cont2 = cont2 + 1
                cont = 0

if __name__ == '__main__' :
	app = QtGui.QApplication([])
	login = Login()
	login.show()
	app.exec_()