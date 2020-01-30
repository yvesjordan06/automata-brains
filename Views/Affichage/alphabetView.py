# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/alphabetView.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Models.Automate import Automate


class Ui_Form(object):
    def __init__(self, automate:Automate):
        self.automate = automate
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(180, 285)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.alphabetDisplayGroup = QtWidgets.QGroupBox(Form)
        self.alphabetDisplayGroup.setObjectName("alphabetDisplayGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.alphabetDisplayGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.etatList = QtWidgets.QListWidget(self.alphabetDisplayGroup)
        self.etatList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.etatList.setUniformItemSizes(False)
        self.etatList.setObjectName("etatList")

        self.verticalLayout.addWidget(self.etatList)
        self.remove = QtWidgets.QPushButton(self.alphabetDisplayGroup)
        self.remove.setStyleSheet("padding:8px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove.setIcon(icon)
        self.remove.setObjectName("remove")
        self.verticalLayout.addWidget(self.remove)
        self.horizontalLayout.addWidget(self.alphabetDisplayGroup)

        self.retranslateUi(Form)
        self.etatList.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Initial Set State
        self.action_set_state()

        #Binding
        self.remove.clicked.connect(self.action_delete_symbole)
        self.automate.automate_modifier.connect(self.action_set_state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.alphabetDisplayGroup.setTitle(_translate("Form", "Alphabet"))
        self.etatList.setSortingEnabled(True)
        __sortingEnabled = self.etatList.isSortingEnabled()
        self.etatList.setSortingEnabled(False)

        self.etatList.setSortingEnabled(__sortingEnabled)
        self.remove.setText(_translate("Form", "Supprimer"))

    def action_set_state(self):
        self.etatList.clear()
        self.etatList.addItems(self.automate.alphabet.list)

    def action_delete_symbole(self):
        selected = self.etatList.selectedItems()
        selected_symbols = [s.text() for s in selected]

        self.etatList.reset()

        for symbole in selected_symbols:
            #TODO Bind this method to automate delete symbol instead
            self.automate.alphabet.supprime_symbole(symbole)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
