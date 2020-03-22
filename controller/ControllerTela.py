from PyQt5.QtWidgets import QMainWindow
from view.tela import Ui_MainWindow

class ControllerTela(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)

