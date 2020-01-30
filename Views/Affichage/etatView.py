# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/etatsView.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from Models.Automate import Automate
from Models.Etat import Etat


class Ui_Form(object):
    def __init__(self, automate: Automate):
        self.automate = automate
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(386, 254)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.alphabetDisplayGroup = QtWidgets.QGroupBox(Form)
        self.alphabetDisplayGroup.setObjectName("alphabetDisplayGroup")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.alphabetDisplayGroup)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.etatList = QtWidgets.QListWidget(self.alphabetDisplayGroup)
        self.etatList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.etatList.setUniformItemSizes(False)
        self.etatList.setObjectName("etatList")

        self.horizontalLayout_2.addWidget(self.etatList)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.setInitial = QtWidgets.QPushButton(self.alphabetDisplayGroup)
        self.setInitial.setStyleSheet("padding:8px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/initial.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setInitial.setIcon(icon)
        self.setInitial.setObjectName("setInitial")
        self.verticalLayout.addWidget(self.setInitial)
        self.setFinal = QtWidgets.QPushButton(self.alphabetDisplayGroup)
        self.setFinal.setStyleSheet("padding:8px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/final.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setFinal.setIcon(icon1)
        self.setFinal.setObjectName("setFinal")
        self.verticalLayout.addWidget(self.setFinal)
        self.remove = QtWidgets.QPushButton(self.alphabetDisplayGroup)
        self.remove.setStyleSheet("padding:8px")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove.setIcon(icon2)
        self.remove.setObjectName("remove")
        self.verticalLayout.addWidget(self.remove)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.alphabetDisplayGroup)

        self.retranslateUi(Form)
        self.etatList.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Set Initial State
        self.action_set_state()

        #Binding
        self.setInitial.clicked.connect(self.action_toggle_etat_initial)
        self.setFinal.clicked.connect(self.action_toggle_etat_final)
        self.remove.clicked.connect(self.action_supprimer_etat)
        self.automate.automate_modifier.connect(self.action_set_state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.alphabetDisplayGroup.setTitle(_translate("Form", "Etats"))
        self.etatList.setSortingEnabled(True)
        __sortingEnabled = self.etatList.isSortingEnabled()
        self.etatList.setSortingEnabled(False)

        self.etatList.setSortingEnabled(__sortingEnabled)
        self.setInitial.setText(_translate("Form", "Initial"))
        self.setFinal.setText(_translate("Form", "Final"))
        self.remove.setText(_translate("Form", "Supprimer"))

    def action_set_state(self):
        self.etatList.clear()

        for etat in self.automate.etats:
            label = str(etat)
            item = QtWidgets.QListWidgetItem(label)
            initial = False
            final = False
            if etat == self.automate.etat_initial:
                initial = True
            if etat in self.automate.etats_finaux:
                final = True
            if initial:
               item = QtWidgets.QListWidgetItem(QIcon("icons/initial.png"), label)
            if final:
                item = QtWidgets.QListWidgetItem(QIcon("icons/final.png"), label)
            if initial and final:
                item = QtWidgets.QListWidgetItem(QIcon("icons/icon.png"), label)
            self.etatList.addItem(item)

    def action_toggle_etat_initial(self, *args):
        selected = self.etatList.selectedItems()
        if len(selected) == 1:
            etat = Etat(selected[0].text())
            if etat != self.automate.etat_initial:
                self.automate.ajouter_initital(etat)

    def action_toggle_etat_final(self, *args):
        selected = self.etatList.selectedItems()
        for select in selected:
            etat = Etat(select.text())
            if etat in self.automate.etats_finaux:
                #TODO faire le methode pour retirer un etat final
                pass
            else:
                self.automate.ajouter_final(etat)

    def action_supprimer_etat(self):
        selected = self.etatList.selectedItems()
        for select in selected:
            etat = Etat(select.text())
            #TODO Methode pour supprimer un etat
            pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
