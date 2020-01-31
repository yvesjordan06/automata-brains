# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/bigReconnaisance.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GroupBox(object):
    def __init__(self, automate):
        self.automate = automate
        self.automate.reconnaissance.connect(self.setResult)

    def setupUi(self, GroupBox):
        GroupBox.setObjectName("GroupBox")
        GroupBox.resize(292, 269)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 181, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 181, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 181, 238))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        GroupBox.setPalette(palette)
        GroupBox.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(GroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(GroupBox)
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(13)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.pushButton = QtWidgets.QPushButton(GroupBox)
        self.pushButton.setStyleSheet("padding:8px")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)


        self.pushButton.clicked.connect(self.ask_reconnaissance)

    def retranslateUi(self, GroupBox):
        _translate = QtCore.QCoreApplication.translate

        #GroupBox.setTitle(_translate("GroupBox", "Reconnaissance"))
        self.pushButton.setText(_translate("GroupBox", "Reconnaitre"))

    def setResult(self, text):
        self.plainTextEdit.clear()
        self.plainTextEdit.setPlainText(text)

    def ask_reconnaissance(self):
        text = self.plainTextEdit.toPlainText()
        result = self.automate.reconnais_text(text)
        self.automate.reconnaissance.emit(result)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GroupBox = QtWidgets.QGroupBox()
    ui = Ui_GroupBox()
    ui.setupUi(GroupBox)
    GroupBox.show()
    sys.exit(app.exec_())
