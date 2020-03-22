from model.ModelTela import ModelTela
from controller.ControllerTela import ControllerTela
from PyQt5.QtWidgets import QApplication

import sys

class CalculoDePorcentagens(QApplication):
    def __init__(self, sys_argv):
        super(CalculoDePorcentagens, self).__init__(sys_argv)
        self.model = ModelTela()
        self.view = ControllerTela(self.model)
        self.view.show()


if __name__ == "__main__":
    app = CalculoDePorcentagens(sys.argv)
    sys.exit(app.exec())
