# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/transitionView.ui'
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
        Form.resize(369, 279)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setObjectName("tableWidget")

        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Initial Set State
        self.action_set_state()

        self.automate.automate_modifier.connect(self.action_set_state)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Transition"))
        self.label.setText(_translate("Form", "Alphabet"))
        self.label_2.setText(_translate("Form", "Etats"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def action_set_state(self):
        self.tableWidget.clear()
        etat_list = list(self.automate.etats)
        etats = [f"{'->' if etat == self.automate.etat_initial else ''}{etat}{'->' if etat in self.automate.etats_finaux else ''}" for etat in etat_list]
        alphabet = [symbole for symbole in self.automate.alphabet.list]
        self.tableWidget.setColumnCount(len(self.automate.alphabet.list))
        self.tableWidget.setRowCount(len(self.automate.etats))
        self.tableWidget.setVerticalHeaderLabels(etats)
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
