# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(458, 339)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 461, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)
        self.pushButton_div = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout.addWidget(self.pushButton_div, 1, 3, 1, 1)
        self.pushButton_C = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_C.setObjectName("pushButton_C")
        self.gridLayout.addWidget(self.pushButton_C, 0, 2, 1, 1)
        self.pushButton_plus = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout.addWidget(self.pushButton_plus, 4, 3, 1, 1)
        self.pushButton_sqr = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_sqr.setObjectName("pushButton_sqr")
        self.gridLayout.addWidget(self.pushButton_sqr, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_minus = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.gridLayout.addWidget(self.pushButton_minus, 3, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 4, 2, 1, 1)
        self.pushButton_sqrt = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_sqrt.setObjectName("pushButton_sqrt")
        self.gridLayout.addWidget(self.pushButton_sqrt, 1, 2, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 2, 0, 1, 1)
        self.pushButton_del = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_del.setObjectName("pushButton_del")
        self.gridLayout.addWidget(self.pushButton_del, 0, 3, 1, 1)
        self.pushButton_mul = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.gridLayout.addWidget(self.pushButton_mul, 2, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.pushButton_percent = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.gridLayout.addWidget(self.pushButton_percent, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 3, 2, 1, 1)
        self.pushButton_rev = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_rev.setObjectName("pushButton_rev")
        self.gridLayout.addWidget(self.pushButton_rev, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 4, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 4, 0, 1, 1)
        self.pushButton_sad = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_sad.setObjectName("pushButton_sad")
        self.gridLayout.addWidget(self.pushButton_sad, 0, 1, 1, 1)
        self.pushButton_happy = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_happy.setObjectName("pushButton_happy")
        self.gridLayout.addWidget(self.pushButton_happy, 5, 0, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 5, 1, 1, 1)
        self.pushButton_dot = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.gridLayout.addWidget(self.pushButton_dot, 5, 2, 1, 1)
        self.pushButton_eq = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_eq.setObjectName("pushButton_eq")
        self.gridLayout.addWidget(self.pushButton_eq, 5, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_div.setText(_translate("Form", "/"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.pushButton_plus.setText(_translate("Form", "+"))
        self.pushButton_sqr.setText(_translate("Form", "x^2"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_minus.setText(_translate("Form", "-"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_9.setText(_translate("Form", "9"))
        self.pushButton_sqrt.setText(_translate("Form", "x^1/2"))
        self.pushButton_1.setText(_translate("Form", "1"))
        self.pushButton_del.setText(_translate("Form", "DEL"))
        self.pushButton_mul.setText(_translate("Form", "*"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_percent.setText(_translate("Form", "%"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_rev.setText(_translate("Form", "1/x"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_sad.setText(_translate("Form", ":("))
        self.pushButton_happy.setText(_translate("Form", ":)"))
        self.pushButton_0.setText(_translate("Form", "0"))
        self.pushButton_dot.setText(_translate("Form", "."))
        self.pushButton_eq.setText(_translate("Form", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
