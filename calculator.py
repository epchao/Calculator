import PyQt5.QtWidgets as qtw 
import sys

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator') 
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []

        self.show()

    def keypad(self):
        container = qtw.QWidget()    
        container.setLayout(qtw.QGridLayout())

        # Buttons
        self.result = qtw.QLineEdit()
        button_result = qtw.QPushButton('Enter', clicked = self.func_result)
        button_clear = qtw.QPushButton('Clear', clicked = self.clear_calc)
        button_9 = qtw.QPushButton('9', clicked = lambda:self.num_press('9'))
        button_8 = qtw.QPushButton('8', clicked = lambda:self.num_press('8'))
        button_7 = qtw.QPushButton('7', clicked = lambda:self.num_press('7'))
        button_6 = qtw.QPushButton('6', clicked = lambda:self.num_press('6'))
        button_5 = qtw.QPushButton('5', clicked = lambda:self.num_press('5'))
        button_4 = qtw.QPushButton('4', clicked = lambda:self.num_press('4'))
        button_3 = qtw.QPushButton('3', clicked = lambda:self.num_press('3'))
        button_2 = qtw.QPushButton('2', clicked = lambda:self.num_press('2'))
        button_1 = qtw.QPushButton('1', clicked = lambda:self.num_press('1'))
        button_0 = qtw.QPushButton('0', clicked = lambda:self.num_press('0'))
        button_plus = qtw.QPushButton('+', clicked = lambda:self.func_press('+'))
        button_minus = qtw.QPushButton('-', clicked = lambda:self.func_press('-'))
        button_multiply = qtw.QPushButton('*', clicked = lambda:self.func_press('*'))
        button_divide = qtw.QPushButton('÷', clicked = lambda:self.func_press('/'))

        # Layout
        container.layout().addWidget(self.result, 0, 0, 1, 4)
        container.layout().addWidget(button_result, 1, 0, 1, 2)
        container.layout().addWidget(button_clear, 1, 2, 1, 2)
        container.layout().addWidget(button_9, 2, 0)
        container.layout().addWidget(button_8, 2, 1)
        container.layout().addWidget(button_7, 2, 2)
        container.layout().addWidget(button_plus, 2,3)
        container.layout().addWidget(button_6, 3, 0)
        container.layout().addWidget(button_5, 3, 1)
        container.layout().addWidget(button_4, 3, 2)
        container.layout().addWidget(button_minus, 3, 3)
        container.layout().addWidget(button_3, 4, 0)
        container.layout().addWidget(button_2, 4, 1)
        container.layout().addWidget(button_1, 4, 2)
        container.layout().addWidget(button_multiply, 4, 3)
        container.layout().addWidget(button_0, 5, 0, 1, 3)
        container.layout().addWidget(button_divide, 5, 3)
        self.layout().addWidget(container)

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.result.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.result.setText(temp_string)

    def func_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result.setText(''.join(self.fin_nums))

    def func_result(self):
        try: 
            fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
            if fin_string == '' or self.temp_nums == []:
                self.result.setText('ERROR')
            else:
                result_string = eval(fin_string)
                fin_string += '='
                fin_string += str(result_string)
                self.result.setText(fin_string)  
        except ZeroDivisionError: 
            self.result.setText('ERROR')
        
    def clear_calc(self):
        self.result.clear()
        self.temp_nums = []
        self.fin_nums = []

app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()