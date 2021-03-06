from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLabel
from view.telaSistema import  Ui_MainWindow

class ControllerTela(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)

        self.tela.botaoAplicar.clicked.connect(self.aplicarValores)

    def aplicarValores(self):
        try:
            
            atual = float(self.removePontos(self.tela.entradaValorAtual.text()))
            try:
                porcentagem = float(self.removePontos(self.tela.entradaPorcentagem.text()))
            except:
                porcentagem = 0
            try:
                objetivo = float(self.removePontos(self.tela.entradaValorObjetivo.text()))
            except:
                objetivo = 0

            if objetivo != 0:
                diferenca = objetivo - atual
                porcentagem = (100 * diferenca)/atual
                self.tela.entradaPorcentagem.setText("{0:.3f}".format(porcentagem))
            else:
                montante = porcentagem*(atual/100)
                if self.tela.marcarAcrescimo.isChecked():
                    resultado = atual + montante
                else:
                    resultado = atual - montante

                self.tela.entradaValorObjetivo.setText(str(resultado)) 
        except:
            pass
    
    def removePontos(self, texto):
        antiga = list(texto)
        nova = ""
        for caractere in range(len(antiga)):
            if antiga[caractere] == ",":
                nova+="."
            else:
                nova+=antiga[caractere]
        return nova