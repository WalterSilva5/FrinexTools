from PyQt5.QtWidgets import QMainWindow
from view.tela import Ui_MainWindow
import os
from sys import path

class ControllerTela(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)
        self.tela.porcentagemParaDescontos.clicked.connect(self.abre1CalcularPorcentagemParaDescontos)
        self.tela.formatarNumerosParaNotas.clicked.connect(self.abreFormatarNumerosParaNotas)


    def abre1CalcularPorcentagemParaDescontos(self):
        caminho = path[0]+"/modulos/calculoDePorcentagens/CalculoDePorcentagens.pyw"
        os.system("python "+caminho)

    def abreFormatarNumerosParaNotas(self):
        caminho = path[0]+"/modulos/formatarChavesDeNotas/FormatarChavesDeNotas.pyw"
        os.system("python "+caminho)
