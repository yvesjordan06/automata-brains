from PyQt5 import QtWidgets

from Models.Alphabet import Alphabet
from Models.Automate import Automate
from Views.Creation.transitionAddUI import Ui_Form
from Views.Creation.etatUI import Ui_Form as EtatUI
from Views.Creation.alphabetUI import Ui_Form as AlphabetUI


class AddTransitionWindow(QtWidgets.QWidget):


    def __init__(self, automate:Automate):
        super(AddTransitionWindow, self).__init__()

        self.ui = Ui_Form(automate)

        self.ui.setupUi(self)

class AddEtatWindow(QtWidgets.QWidget):


    def __init__(self, automate:Automate):
        super(AddEtatWindow, self).__init__()

        self.ui = EtatUI(automate)

        self.ui.setupUi(self)

class AddAlphabetWindow(QtWidgets.QWidget):


    def __init__(self, automate:Automate):
        super(AddAlphabetWindow, self).__init__()

        self.ui = AlphabetUI(automate)

        self.ui.setupUi(self)
