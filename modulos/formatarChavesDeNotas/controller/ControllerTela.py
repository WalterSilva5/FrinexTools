from PyQt5.QtWidgets import QMainWindow
from view.tela import Ui_MainWindow

class ControllerTela(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)

        self.tela.botaoFormatar.clicked.connect(self.mostrarChaveSaida)

    def mostrarChaveSaida(self):
        chaveEntrada = list(self.tela.chaveEntrada.text())
        chaveSaida = ""
        for caractere in chaveEntrada:
            try:
                if int(caractere) == int(caractere):
                    chaveSaida+=caractere
            except:
                pass
        self.tela.chaveSaida.setText(chaveSaida)
