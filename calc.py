from PyQt6 import QtWidgets
from calc_ui import Ui_Form
from PyQt6.QtCore import Qt

class Window(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.lineEdit.setText('0')

        self.cur = 0
        self.next = 0

        self.ops = ['+', '-', '*', '/', '%', '**0.5', '**2', '**(-1)', '.']

        numbers = [self.ui.pushButton_0, self.ui.pushButton_1, self.ui.pushButton_2,
                        self.ui.pushButton_3, self.ui.pushButton_4, self.ui.pushButton_5,
                        self.ui.pushButton_6, self.ui.pushButton_7, self.ui.pushButton_8,
                        self.ui.pushButton_9]
        
        for i in range(10):
            self.connect_button_number(numbers[i], i)

        operations = [self.ui.pushButton_plus, self.ui.pushButton_minus, self.ui.pushButton_mul, self.ui.pushButton_div, self.ui.pushButton_percent, 
                      self.ui.pushButton_sqrt, self.ui.pushButton_sqr, self.ui.pushButton_rev, self.ui.pushButton_dot]

        for i in range(len(operations)):
            self.connect_button_operation(operations[i], i)

        self.ui.pushButton_C.clicked.connect(self.C)
        self.ui.pushButton_del.clicked.connect(self.delete) 
        self.ui.pushButton_eq.clicked.connect(self.eq)   

    def C(self):
        self.ui.lineEdit.setText('0')

    def delete(self):
        s = self.ui.lineEdit.displayText()
        if (s[-2] == '.'):
            self.ui.lineEdit.setText(s[:-2])
        else:
            self.ui.lineEdit.setText(s[:-1])

        if (len(self.ui.lineEdit.displayText()) == 0):
            self.ui.lineEdit.setText('0')
        
    def connect_button_operation(self, button, number):
        button.clicked.connect(lambda: self.arithmetic_operation(number))

    def arithmetic_operation(self, oper):
        self.cur = self.next
        self.next = 0

        text = self.ui.lineEdit.displayText()

        if text[-1] not in self.ops:
            text += self.ops[oper]
            self.ui.lineEdit.setText(text)

    def eq(self):
        text = self.ui.lineEdit.displayText()

        self.cur = eval(text)
        self.next = 0

        self.ui.lineEdit.setText(str(self.cur))


    def connect_button_number(self, button, number):
        button.clicked.connect(lambda: self.change_number(number))

    def change_number(self, number):
        text = self.ui.lineEdit.displayText()
        last_num = self.next

        self.next *= 10
        self.next += number

        new_text = text + str(self.next)[-1]

        if self.next != last_num:
            if text == '0':
                self.ui.lineEdit.setText(str(self.next)[-1])
            else:
                self.ui.lineEdit.setText(new_text)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.exec()
