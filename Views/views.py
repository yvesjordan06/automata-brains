from PyQt5 import QtWidgets

from Models.Automate import Automate
from Views.Creation.creation import CreationView
from Views.Affichage.see import Ui_Form as SeeView


class CreateAutomataView(QtWidgets.QWidget):


    def __init__(self, automate:Automate, list:dict):
        super(CreateAutomataView, self).__init__()

        self.ui = CreationView(automate, list)

        self.ui.setupUi(self)

class SeeAutomataView(QtWidgets.QWidget):


    def __init__(self, automate:Automate, list):
        super(SeeAutomataView, self).__init__()

        self.ui = SeeView(automate, list)

        self.ui.setupUi(self)
