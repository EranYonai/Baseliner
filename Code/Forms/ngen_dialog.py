# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ngen_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(774, 555)
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(240, 20, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.confirm_button = QtWidgets.QPushButton(Dialog)
        self.confirm_button.setGeometry(QtCore.QRect(600, 490, 93, 28))
        self.confirm_button.setObjectName("confirm_button")
        self.check_button = QtWidgets.QPushButton(Dialog)
        self.check_button.setGeometry(QtCore.QRect(440, 490, 93, 28))
        self.check_button.setObjectName("check_button")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 100, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.consoleSN_text = QtWidgets.QLineEdit(Dialog)
        self.consoleSN_text.setGeometry(QtCore.QRect(180, 100, 191, 22))
        self.consoleSN_text.setObjectName("consoleSN_text")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.consolePN_text = QtWidgets.QLineEdit(Dialog)
        self.consolePN_text.setGeometry(QtCore.QRect(180, 130, 191, 22))
        self.consolePN_text.setObjectName("consolePN_text")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.consoleV_text = QtWidgets.QLineEdit(Dialog)
        self.consoleV_text.setGeometry(QtCore.QRect(180, 160, 191, 22))
        self.consoleV_text.setObjectName("consoleV_text")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.psuSN_text = QtWidgets.QLineEdit(Dialog)
        self.psuSN_text.setGeometry(QtCore.QRect(180, 190, 191, 22))
        self.psuSN_text.setObjectName("psuSN_text")
        self.psuPN_text = QtWidgets.QLineEdit(Dialog)
        self.psuPN_text.setGeometry(QtCore.QRect(180, 220, 191, 22))
        self.psuPN_text.setObjectName("psuPN_text")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 250, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.monitor1PN_text = QtWidgets.QLineEdit(Dialog)
        self.monitor1PN_text.setGeometry(QtCore.QRect(560, 120, 191, 22))
        self.monitor1PN_text.setObjectName("monitor1PN_text")
        self.monitor1V_text = QtWidgets.QLineEdit(Dialog)
        self.monitor1V_text.setGeometry(QtCore.QRect(560, 150, 191, 22))
        self.monitor1V_text.setObjectName("monitor1V_text")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(390, 120, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.psuCable_text = QtWidgets.QLineEdit(Dialog)
        self.psuCable_text.setGeometry(QtCore.QRect(180, 250, 191, 22))
        self.psuCable_text.setObjectName("psuCable_text")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(390, 90, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 280, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.monitor1SN_text = QtWidgets.QLineEdit(Dialog)
        self.monitor1SN_text.setGeometry(QtCore.QRect(560, 90, 191, 22))
        self.monitor1SN_text.setObjectName("monitor1SN_text")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(390, 150, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.genToPiu_text = QtWidgets.QLineEdit(Dialog)
        self.genToPiu_text.setGeometry(QtCore.QRect(180, 280, 191, 22))
        self.genToPiu_text.setObjectName("genToPiu_text")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(390, 210, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.monitor2HubSN_text = QtWidgets.QLineEdit(Dialog)
        self.monitor2HubSN_text.setGeometry(QtCore.QRect(180, 420, 191, 22))
        self.monitor2HubSN_text.setObjectName("monitor2HubSN_text")
        self.monitor1PsuPN_text = QtWidgets.QLineEdit(Dialog)
        self.monitor1PsuPN_text.setGeometry(QtCore.QRect(560, 270, 191, 22))
        self.monitor1PsuPN_text.setObjectName("monitor1PsuPN_text")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(20, 450, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(20, 420, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.monitor2SN_text = QtWidgets.QLineEdit(Dialog)
        self.monitor2SN_text.setGeometry(QtCore.QRect(180, 330, 191, 22))
        self.monitor2SN_text.setObjectName("monitor2SN_text")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(20, 330, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(390, 270, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(390, 240, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.monitor2HubPN_text = QtWidgets.QLineEdit(Dialog)
        self.monitor2HubPN_text.setGeometry(QtCore.QRect(180, 450, 191, 22))
        self.monitor2HubPN_text.setObjectName("monitor2HubPN_text")
        self.monitor1HubSN_text = QtWidgets.QLineEdit(Dialog)
        self.monitor1HubSN_text.setGeometry(QtCore.QRect(560, 180, 191, 22))
        self.monitor1HubSN_text.setObjectName("monitor1HubSN_text")
        self.monitor1HubPN_text = QtWidgets.QLineEdit(Dialog)
        self.monitor1HubPN_text.setGeometry(QtCore.QRect(560, 210, 191, 22))
        self.monitor1HubPN_text.setObjectName("monitor1HubPN_text")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(20, 480, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.monitor2PN_text = QtWidgets.QLineEdit(Dialog)
        self.monitor2PN_text.setGeometry(QtCore.QRect(180, 360, 191, 22))
        self.monitor2PN_text.setObjectName("monitor2PN_text")
        self.monitor1PsuSN_text = QtWidgets.QLineEdit(Dialog)
        self.monitor1PsuSN_text.setGeometry(QtCore.QRect(560, 240, 191, 22))
        self.monitor1PsuSN_text.setObjectName("monitor1PsuSN_text")
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(390, 180, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(20, 360, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.monitor2PsuSN_text = QtWidgets.QLineEdit(Dialog)
        self.monitor2PsuSN_text.setGeometry(QtCore.QRect(180, 480, 191, 22))
        self.monitor2PsuSN_text.setObjectName("monitor2PsuSN_text")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(20, 390, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.monitor2V_text = QtWidgets.QLineEdit(Dialog)
        self.monitor2V_text.setGeometry(QtCore.QRect(180, 390, 191, 22))
        self.monitor2V_text.setObjectName("monitor2V_text")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(390, 360, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.pumptoConsoleCable_text = QtWidgets.QLineEdit(Dialog)
        self.pumptoConsoleCable_text.setGeometry(QtCore.QRect(560, 420, 191, 22))
        self.pumptoConsoleCable_text.setObjectName("pumptoConsoleCable_text")
        self.label_22 = QtWidgets.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(390, 330, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.ngenPumpV_text = QtWidgets.QLineEdit(Dialog)
        self.ngenPumpV_text.setGeometry(QtCore.QRect(560, 390, 191, 22))
        self.ngenPumpV_text.setObjectName("ngenPumpV_text")
        self.ngenPumpSN_text = QtWidgets.QLineEdit(Dialog)
        self.ngenPumpSN_text.setGeometry(QtCore.QRect(560, 330, 191, 22))
        self.ngenPumpSN_text.setObjectName("ngenPumpSN_text")
        self.monitor2PsuPN_text = QtWidgets.QLineEdit(Dialog)
        self.monitor2PsuPN_text.setGeometry(QtCore.QRect(180, 510, 191, 22))
        self.monitor2PsuPN_text.setObjectName("monitor2PsuPN_text")
        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(20, 510, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(390, 390, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.ngenPumpPN_text = QtWidgets.QLineEdit(Dialog)
        self.ngenPumpPN_text.setGeometry(QtCore.QRect(560, 360, 191, 22))
        self.ngenPumpPN_text.setObjectName("ngenPumpPN_text")
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(390, 420, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.foot_pedal_text = QtWidgets.QLineEdit(Dialog)
        self.foot_pedal_text.setGeometry(QtCore.QRect(560, 450, 191, 22))
        self.foot_pedal_text.setText("")
        self.foot_pedal_text.setObjectName("foot_pedal_text")
        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(390, 450, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Product Sans Light")
        font.setPointSize(9)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.consoleSN_text, self.consolePN_text)
        Dialog.setTabOrder(self.consolePN_text, self.consoleV_text)
        Dialog.setTabOrder(self.consoleV_text, self.psuSN_text)
        Dialog.setTabOrder(self.psuSN_text, self.psuPN_text)
        Dialog.setTabOrder(self.psuPN_text, self.psuCable_text)
        Dialog.setTabOrder(self.psuCable_text, self.genToPiu_text)
        Dialog.setTabOrder(self.genToPiu_text, self.monitor1SN_text)
        Dialog.setTabOrder(self.monitor1SN_text, self.monitor1PN_text)
        Dialog.setTabOrder(self.monitor1PN_text, self.monitor1V_text)
        Dialog.setTabOrder(self.monitor1V_text, self.monitor1HubSN_text)
        Dialog.setTabOrder(self.monitor1HubSN_text, self.monitor1HubPN_text)
        Dialog.setTabOrder(self.monitor1HubPN_text, self.monitor1PsuSN_text)
        Dialog.setTabOrder(self.monitor1PsuSN_text, self.monitor1PsuPN_text)
        Dialog.setTabOrder(self.monitor1PsuPN_text, self.monitor2SN_text)
        Dialog.setTabOrder(self.monitor2SN_text, self.monitor2PN_text)
        Dialog.setTabOrder(self.monitor2PN_text, self.monitor2V_text)
        Dialog.setTabOrder(self.monitor2V_text, self.monitor2HubSN_text)
        Dialog.setTabOrder(self.monitor2HubSN_text, self.monitor2HubPN_text)
        Dialog.setTabOrder(self.monitor2HubPN_text, self.monitor2PsuSN_text)
        Dialog.setTabOrder(self.monitor2PsuSN_text, self.monitor2PsuPN_text)
        Dialog.setTabOrder(self.monitor2PsuPN_text, self.ngenPumpSN_text)
        Dialog.setTabOrder(self.ngenPumpSN_text, self.ngenPumpPN_text)
        Dialog.setTabOrder(self.ngenPumpPN_text, self.ngenPumpV_text)
        Dialog.setTabOrder(self.ngenPumpV_text, self.pumptoConsoleCable_text)
        Dialog.setTabOrder(self.pumptoConsoleCable_text, self.foot_pedal_text)
        Dialog.setTabOrder(self.foot_pedal_text, self.check_button)
        Dialog.setTabOrder(self.check_button, self.confirm_button)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "nGEN RF Generator"))
        self.confirm_button.setText(_translate("Dialog", "Confirm"))
        self.check_button.setText(_translate("Dialog", "Verify"))
        self.label.setText(_translate("Dialog", "Console S.N: "))
        self.label_2.setText(_translate("Dialog", "Console P.N:"))
        self.label_3.setText(_translate("Dialog", "Console Version:"))
        self.label_4.setText(_translate("Dialog", "PSU S.N:"))
        self.label_5.setText(_translate("Dialog", "PSU P.N:"))
        self.label_6.setText(_translate("Dialog", "PSU Cable:"))
        self.label_7.setText(_translate("Dialog", "Monitor #1 PN:"))
        self.label_8.setText(_translate("Dialog", "Monitor #1 S.N:"))
        self.label_9.setText(_translate("Dialog", "Generator to PIU Cable:"))
        self.label_10.setText(_translate("Dialog", "Monitor #1 Ver:"))
        self.label_11.setText(_translate("Dialog", "Monitor #1 Hub P.N:"))
        self.label_12.setText(_translate("Dialog", "Monitor #2 Hub P.N:"))
        self.label_13.setText(_translate("Dialog", "Monitor #2 Hub S.N:"))
        self.label_14.setText(_translate("Dialog", "Monitor #2 S.N:"))
        self.label_15.setText(_translate("Dialog", "Monitor #1 PSU PN:"))
        self.label_16.setText(_translate("Dialog", "Monitor #1 PSU S.N:"))
        self.label_17.setText(_translate("Dialog", "Monitor #2 PSU S.N:"))
        self.label_18.setText(_translate("Dialog", "Monitor #1 Hub S.N:"))
        self.label_19.setText(_translate("Dialog", "Monitor #2 P.N:"))
        self.label_20.setText(_translate("Dialog", "Monitor #2 Version:"))
        self.label_21.setText(_translate("Dialog", "nGEN Pump P.N:"))
        self.label_22.setText(_translate("Dialog", "nGEN Pump S.N:"))
        self.label_23.setText(_translate("Dialog", "Monitor #2 PSU P.N:"))
        self.label_24.setText(_translate("Dialog", "nGEN Pump Version:"))
        self.label_25.setText(_translate("Dialog", "Pump to Console Cable:"))
        self.label_26.setText(_translate("Dialog", "Foot Pedal:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
