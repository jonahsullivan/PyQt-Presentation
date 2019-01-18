# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello_world_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelloWorldDialogBase(object):
    def setupUi(self, HelloWorldDialogBase):
        HelloWorldDialogBase.setObjectName("HelloWorldDialogBase")
        HelloWorldDialogBase.resize(477, 235)
        self.gridLayout_2 = QtWidgets.QGridLayout(HelloWorldDialogBase)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setObjectName("gridLayout")
        self.messageLayout = QtWidgets.QVBoxLayout()
        self.messageLayout.setObjectName("messageLayout")
        self.comboBox = QtWidgets.QComboBox(HelloWorldDialogBase)
        self.comboBox.setObjectName("comboBox")
        self.messageLayout.addWidget(self.comboBox)
        self.messageBox = QtWidgets.QLineEdit(HelloWorldDialogBase)
        self.messageBox.setObjectName("messageBox")
        self.messageLayout.addWidget(self.messageBox)
        self.gridLayout.addLayout(self.messageLayout, 2, 0, 1, 1)
        self.button_box = QtWidgets.QDialogButtonBox(HelloWorldDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.gridLayout.addWidget(self.button_box, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(HelloWorldDialogBase)
        self.button_box.accepted.connect(HelloWorldDialogBase.accept)
        self.button_box.rejected.connect(HelloWorldDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(HelloWorldDialogBase)
        HelloWorldDialogBase.setTabOrder(self.button_box, self.messageBox)

    def retranslateUi(self, HelloWorldDialogBase):
        _translate = QtCore.QCoreApplication.translate
        HelloWorldDialogBase.setWindowTitle(_translate("HelloWorldDialogBase", "Hello World"))
        self.messageBox.setText(_translate("HelloWorldDialogBase", "Messages: None"))

