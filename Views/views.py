from PyQt5 import QtWidgets

from Models.Automate import Automate
from Views.Creation.creation import CreationView
from Views.Affichage.see import Ui_Form as SeeView


class CreateAutomataView(QtWidgets.QWidget):


    def __init__(self, automate:Automate):
        super(CreateAutomataView, self).__init__()

        self.ui = CreationView(automate)

        self.ui.setupUi(self)

class SeeAutomataView(QtWidgets.QWidget):


    def __init__(self, automate:Automate):
        super(SeeAutomataView, self).__init__()

        self.ui = SeeView(automate)

        self.ui.setupUi(self)
