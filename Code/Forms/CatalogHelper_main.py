# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CatalogHelper_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(368, 129)
        self.signelCatalog_Text = QtWidgets.QLineEdit(Dialog)
        self.signelCatalog_Text.setGeometry(QtCore.QRect(50, 80, 191, 21))
        self.signelCatalog_Text.setObjectName("signelCatalog_Text")
        self.getCatalog_B = QtWidgets.QPushButton(Dialog)
        self.getCatalog_B.setGeometry(QtCore.QRect(250, 74, 93, 28))
        self.getCatalog_B.setAutoDefault(True)
        self.getCatalog_B.setDefault(True)
        self.getCatalog_B.setObjectName("getCatalog_B")
        #self.signelCatalog_Text.returnPressed.connect(self.getCatalog_B.click)
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(80, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.getCatalog_B.setText(_translate("Dialog", "Get Catalog"))
        self.title.setText(_translate("Dialog", "Catalog Helper"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())