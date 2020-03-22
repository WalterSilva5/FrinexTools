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
        MainWindow.resize(1080, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.modulosFrame = QtWidgets.QFrame(self.centralwidget)
        self.modulosFrame.setGeometry(QtCore.QRect(10, 10, 331, 781))
        self.modulosFrame.setStyleSheet("background-color: rgb(206, 202, 255);\n"
"border-radius: 10px;")
        self.modulosFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.modulosFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.modulosFrame.setObjectName("modulosFrame")
        self.entradaModulos = QtWidgets.QTextEdit(self.modulosFrame)
        self.entradaModulos.setGeometry(QtCore.QRect(10, 50, 311, 51))
        self.entradaModulos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.entradaModulos.setObjectName("entradaModulos")
        self.labelModulos = QtWidgets.QLabel(self.modulosFrame)
        self.labelModulos.setGeometry(QtCore.QRect(80, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelModulos.setFont(font)
        self.labelModulos.setObjectName("labelModulos")
        self.frame = QtWidgets.QFrame(self.modulosFrame)
        self.frame.setGeometry(QtCore.QRect(10, 110, 311, 661))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.listaBotoes = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.listaBotoes.setContentsMargins(0, 0, 0, 0)
        self.listaBotoes.setObjectName("listaBotoes")
        self.porcentagemParaDescontos = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.porcentagemParaDescontos.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.porcentagemParaDescontos.setFont(font)
        self.porcentagemParaDescontos.setStyleSheet("background-color: rgb(255, 116, 116);\n"
"\n"
"")
        self.porcentagemParaDescontos.setObjectName("porcentagemParaDescontos")
        self.listaBotoes.addWidget(self.porcentagemParaDescontos)
        self.formatarNumerosParaNotas = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.formatarNumerosParaNotas.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.formatarNumerosParaNotas.setFont(font)
        self.formatarNumerosParaNotas.setStyleSheet("background-color: rgb(255, 116, 116);")
        self.formatarNumerosParaNotas.setObjectName("formatarNumerosParaNotas")
        self.listaBotoes.addWidget(self.formatarNumerosParaNotas)
        self.frameInicial = QtWidgets.QFrame(self.centralwidget)
        self.frameInicial.setGeometry(QtCore.QRect(350, 10, 721, 781))
        self.frameInicial.setStyleSheet("background-color: rgb(206, 202, 255);\n"
"border-radius: 10px;")
        self.frameInicial.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameInicial.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameInicial.setObjectName("frameInicial")
        self.labelTitulo = QtWidgets.QLabel(self.frameInicial)
        self.labelTitulo.setGeometry(QtCore.QRect(40, 290, 661, 161))
        font = QtGui.QFont()
        font.setPointSize(68)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Frinex Tools"))
        self.labelModulos.setText(_translate("MainWindow", "MODULOS"))
        self.porcentagemParaDescontos.setText(_translate("MainWindow", "1 - Porcentagem Para Descontos"))
        self.formatarNumerosParaNotas.setText(_translate("MainWindow", "2 - formatarNumerosParaNotas"))
        self.labelTitulo.setText(_translate("MainWindow", "FRINEX TOOLS"))
