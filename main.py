#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.uic import loadUiType
import threading
from get import *
from verify_login import *

Ui_MainWindow, QMainWindow = loadUiType('ui/main.ui')
Ui_LoginWindow, QLoginWindow = loadUiType('ui/login.ui')

class Login(QLoginWindow, Ui_LoginWindow):
    def __init__(self, parent=None):
        QLoginWindow.__init__(self, parent)
        self.setupUi(self)

        self.curso = "1"
        self.matr = ""
        self.senha = ""

    def on_lineEdit_textEdited(self, text):
        self.matr = text
        self.frame.lower()

    def on_lineEdit_2_textEdited(self, text):
        self.senha = text
        self.frame.lower()

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

        # Bloco UTF8 para setar o texto corretamente no software.
        try:
            _fromUtf8 = QtCore.QString.fromUtf8
        except AttributeError:
            def _fromUtf8(s):
                return s

        if self.matr == "":
            if self.senha == "":
                self.label_6.setText(_fromUtf8("Preencha o número de matrícula e a senha."))
                self.frame.raise_()
            else:
                self.label_6.setText(_fromUtf8("Preencha o número de matrícula."))
                self.frame.raise_()

        if self.senha == "":
            if self.matr != "":
                self.label_6.setText(_fromUtf8("Preencha a senha."))
                self.frame.raise_()

        if self.senha and self.matr != "":
            if verify(self.curso, self.matr, self.senha) == True:
                self.principal = Main(self.matr, self.senha, self.curso)

                # Nesse esquema de threading é obrigatório passar dois argumentos na tupla.
                threading._start_new_thread(self.principal.horario, ("Thread Horario", 1))
                threading._start_new_thread(self.principal.provas, ("Thread Provas", 2))
                threading._start_new_thread(self.principal.historico, ("Thread Historico", 3))

                self.principal.show()

                login.hide()

            else:
                self.label_6.setText(_fromUtf8("Dados de login incorretos!"))
                self.frame.raise_()

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, matr, senha, curso, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.matr = matr
        self.senha = senha
        self.curso = curso

    def provas(self, th, num):
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

    def horario(self, th, num):
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

    def historico(self, th, num):
        lista_historico = get_historico(self.matr, self.senha, self.curso)

        num_itens = len(lista_historico) / 4
        self.tableWidget_3.setRowCount(num_itens)

        cont = cont2 = 0

        for iten in lista_historico:
            item = QtGui.QTableWidgetItem()
            self.tableWidget_3.setItem(cont2, cont, item)
            item.setText("%s" % iten)

            cont = cont + 1

            if cont == 4:
                cont2 = cont2 + 1
                cont = 0

if __name__ == '__main__' :
    import sys
    app = QtGui.QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())