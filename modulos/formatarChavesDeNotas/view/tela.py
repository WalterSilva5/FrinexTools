# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 721, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 120, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 340, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.botaoFormatar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoFormatar.setGeometry(QtCore.QRect(240, 260, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.botaoFormatar.setFont(font)
        self.botaoFormatar.setStyleSheet("background-color: rgb(255, 162, 162)")
        self.botaoFormatar.setObjectName("botaoFormatar")
        self.chaveEntrada = QtWidgets.QLineEdit(self.centralwidget)
        self.chaveEntrada.setGeometry(QtCore.QRect(30, 170, 741, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.chaveEntrada.setFont(font)
        self.chaveEntrada.setText("")
        self.chaveEntrada.setObjectName("chaveEntrada")
        self.chaveSaida = QtWidgets.QLineEdit(self.centralwidget)
        self.chaveSaida.setEnabled(True)
        self.chaveSaida.setGeometry(QtCore.QRect(30, 380, 741, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.chaveSaida.setFont(font)
        self.chaveSaida.setText("")
        self.chaveSaida.setObjectName("chaveSaida")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Frinex Tools - Formatar Notas Fiscais"))
        self.label.setText(_translate("MainWindow", "FORMATAR CHAVES PARA NOTAS FISCAIS"))
        self.label_2.setText(_translate("MainWindow", "COLE AQUI A CHAVE"))
        self.label_3.setText(_translate("MainWindow", "CHAVE FORMATADA"))
        self.botaoFormatar.setText(_translate("MainWindow", "CLIQUE PARA FORMATAR"))
