from PyQt5 import QtWidgets

from Models.Alphabet import Alphabet
from Models.Automate import Automate
from Views.Creation.transitionAddUI import Ui_Form
from Views.Creation.etatUI import Ui_Form as EtatUI
from Views.Creation.alphabetUI import Ui_Form as AlphabetUI
from Views.Creation.automataSelect import Ui_GroupBox as AutomataUI


class AddTransitionWindow(QtWidgets.QWidget):


    def __init__(self, automate:Automate):
        super(AddTransitionWindow, self).__init__()

        self.ui = Ui_Form(automate)

        self.ui.setupUi(self)

class AutomataSelectWindow(QtWidgets.QWidget):


    def __init__(self, automate:Automate, list:dict):
        super(AutomataSelectWindow, self).__init__()

        self.ui = AutomataUI(automate, list)

        self.ui.setupUi(self)

    def setState(self):
        self.ui.set_state()

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
