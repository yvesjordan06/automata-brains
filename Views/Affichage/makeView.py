from PyQt5 import QtWidgets

from Models.Automate import Automate
from Views.Affichage.nomView import Ui_GroupBox as NomUI
from Views.Affichage.etatView import Ui_Form as EtatUI
from Views.Affichage.alphabetView import Ui_Form as AlphabetUI

from Views.Affichage.reconnaissance import Ui_Form as ReconnaissanceUI

from Views.Affichage.central import Ui_TabWidget as CentralUi
from Views.Affichage.typeView import Ui_GroupBox as TypeUI




class SeeCentralWindow(QtWidgets.QTabWidget):


    def __init__(self, automate: Automate):
        super(SeeCentralWindow, self).__init__()

        self.ui = CentralUi(automate)

        self.ui.setupUi(self)




class SeeEtatWindow(QtWidgets.QWidget):


    def __init__(self, automate: Automate):
        super(SeeEtatWindow, self).__init__()

        self.ui = EtatUI(automate)

        self.ui.setupUi(self)

class SeeAlphabetWindow(QtWidgets.QWidget):


    def __init__(self, automate:Automate):
        super(SeeAlphabetWindow, self).__init__()

        self.ui = AlphabetUI(automate)

        self.ui.setupUi(self)

class ReconnaissanceWindow(QtWidgets.QWidget):


    def __init__(self, automate, list):
        super(ReconnaissanceWindow, self).__init__()

        self.ui = ReconnaissanceUI(automate, list)

        self.ui.setupUi(self)
