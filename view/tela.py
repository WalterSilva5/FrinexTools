# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.modulosFrame = QtWidgets.QFrame(self.centralwidget)
        self.modulosFrame.setGeometry(QtCore.QRect(0, 10, 331, 581))
        self.modulosFrame.setStyleSheet("background-color: rgb(206, 202, 255);\n"
"border-radius: 10px;")
        self.modulosFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.modulosFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.modulosFrame.setObjectName("modulosFrame")
        self.labelModulos = QtWidgets.QLabel(self.modulosFrame)
        self.labelModulos.setGeometry(QtCore.QRect(80, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelModulos.setFont(font)
        self.labelModulos.setObjectName("labelModulos")
        self.frame = QtWidgets.QFrame(self.modulosFrame)
        self.frame.setGeometry(QtCore.QRect(10, 110, 311, 461))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 121))
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
"height: 40%;")
        self.porcentagemParaDescontos.setObjectName("porcentagemParaDescontos")
        self.listaBotoes.addWidget(self.porcentagemParaDescontos)
        self.formatarNumerosParaNotas = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.formatarNumerosParaNotas.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.formatarNumerosParaNotas.setFont(font)
        self.formatarNumerosParaNotas.setStyleSheet("background-color: rgb(255, 116, 116);\n"
"height: 40%;")
        self.formatarNumerosParaNotas.setObjectName("formatarNumerosParaNotas")
        self.listaBotoes.addWidget(self.formatarNumerosParaNotas)
        self.lineEdit = QtWidgets.QLineEdit(self.modulosFrame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.frameInicial = QtWidgets.QFrame(self.centralwidget)
        self.frameInicial.setGeometry(QtCore.QRect(350, 10, 641, 581))
        self.frameInicial.setStyleSheet("background-color: rgb(206, 202, 255);\n"
"border-radius: 10px;")
        self.frameInicial.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameInicial.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameInicial.setObjectName("frameInicial")
        self.labelTitulo = QtWidgets.QLabel(self.frameInicial)
        self.labelTitulo.setGeometry(QtCore.QRect(90, 190, 601, 161))
        font = QtGui.QFont()
        font.setPointSize(48)
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
        self.formatarNumerosParaNotas.setText(_translate("MainWindow", "2 - Formatar Chave NF-e"))
        self.labelTitulo.setText(_translate("MainWindow", "FRINEX TOOLS"))
