# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workstation_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_workstation_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(368, 530)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 380, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 245, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 425, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 290, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(100, 10, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.upgradefrom_text = QtWidgets.QLineEdit(Dialog)
        self.upgradefrom_text.setGeometry(QtCore.QRect(160, 110, 191, 22))
        self.upgradefrom_text.setObjectName("upgradefrom_text")
        self.softwarever_text = QtWidgets.QLineEdit(Dialog)
        self.softwarever_text.setGeometry(QtCore.QRect(160, 60, 191, 22))
        self.softwarever_text.setObjectName("softwarever_text")
        self.imagever_text = QtWidgets.QLineEdit(Dialog)
        self.imagever_text.setGeometry(QtCore.QRect(160, 200, 191, 22))
        self.imagever_text.setObjectName("imagever_text")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.wsconf_text = QtWidgets.QLineEdit(Dialog)
        self.wsconf_text.setGeometry(QtCore.QRect(160, 290, 191, 22))
        self.wsconf_text.setObjectName("wsconf_text")
        self.solios_check = QtWidgets.QCheckBox(Dialog)
        self.solios_check.setGeometry(QtCore.QRect(230, 380, 31, 31))
        self.solios_check.setText("")
        self.solios_check.setObjectName("solios_check")
        self.wsmodel_text = QtWidgets.QLineEdit(Dialog)
        self.wsmodel_text.setGeometry(QtCore.QRect(160, 335, 191, 22))
        self.wsmodel_text.setObjectName("wsmodel_text")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 335, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.check_button = QtWidgets.QPushButton(Dialog)
        self.check_button.setGeometry(QtCore.QRect(70, 490, 93, 28))
        self.check_button.setObjectName("check_button")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 155, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.dspver_text = QtWidgets.QLineEdit(Dialog)
        self.dspver_text.setGeometry(QtCore.QRect(160, 155, 191, 22))
        self.dspver_text.setObjectName("dspver_text")
        self.confirm_button = QtWidgets.QPushButton(Dialog)
        self.confirm_button.setGeometry(QtCore.QRect(200, 490, 93, 28))
        self.confirm_button.setObjectName("confirm_button")
        self.servicetag_text = QtWidgets.QLineEdit(Dialog)
        self.servicetag_text.setGeometry(QtCore.QRect(160, 245, 191, 22))
        self.servicetag_text.setObjectName("servicetag_text")
        self.licenses = QtWidgets.QPushButton(Dialog)
        self.licenses.setGeometry(QtCore.QRect(180, 425, 131, 28))
        self.licenses.setObjectName("licenses")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_8.setText(_translate("Dialog", "Solios Card:"))
        self.label_5.setText(_translate("Dialog", "Service Tag:"))
        self.label_9.setText(_translate("Dialog", "Licenses:"))
        self.label_6.setText(_translate("Dialog", "WS Configuration:"))
        self.title.setText(_translate("Dialog", "Work Station"))
        self.label_4.setText(_translate("Dialog", "Image Version:"))
        self.label.setText(_translate("Dialog", "Software Version:"))
        self.label_7.setText(_translate("Dialog", "WS Model:"))
        self.check_button.setText(_translate("Dialog", "Verify"))
        self.label_3.setText(_translate("Dialog", "DSP Version:"))
        self.label_2.setText(_translate("Dialog", "Upgraded from:"))
        self.confirm_button.setText(_translate("Dialog", "Confirm"))
        self.licenses.setText(_translate("Dialog", "Choose Licenses"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_workstation_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())