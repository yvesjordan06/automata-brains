# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/transitionView.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from Models.Automate import Automate


class Ui_Form(object):
    def __init__(self, automate:Automate):
        self.automate = automate

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(369, 279)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")



        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setObjectName("tableWidget")

        self.horizontalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Initial Set State
        self.action_set_state()

        self.automate.automate_modifier.connect(self.action_set_state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        #self.groupBox.setTitle(_translate("Form", "Transition"))


        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def action_set_state(self):
        self.tableWidget.clear()
        etat_list = list(self.automate.etats)
        alphabet = [symbole for symbole in self.automate.alphabet.list]
        self.tableWidget.setColumnCount(len(self.automate.alphabet.list))
        self.tableWidget.setRowCount(len(self.automate.etats))
        row = 0
        for etat in etat_list :
            label = str(etat)
            item = QtWidgets.QTableWidgetItem(label)
            initial = False
            final = False
            if etat == self.automate.etat_initial:
                initial = True
            if etat in self.automate.etats_finaux:
                final = True
            if initial:
                item = QtWidgets.QTableWidgetItem(QIcon("icons/initial.png"), label)
            if final:
                item = QtWidgets.QTableWidgetItem(QIcon("icons/final.png"), label)
            if initial and final:
                item = QtWidgets.QTableWidgetItem(QIcon("icons/icon.png"), label)

            self.tableWidget.setVerticalHeaderItem(row, item)
            row += 1



        self.tableWidget.setHorizontalHeaderLabels(alphabet)

        for t in self.automate.transitions:
            print(t.est_epsilon())
            if (t.est_epsilon()):
                continue
            alphabet_index = alphabet.index(t.symbole)
            etat_index = etat_list.index(t.depart)
            valeur_actu = self.tableWidget.item(etat_index,alphabet_index)
            valeur_text = ' , ' + valeur_actu.text() if valeur_actu else ''
            self.tableWidget.setItem(etat_index, alphabet_index, QtWidgets.QTableWidgetItem(f"{t.arrive}{valeur_text}"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
